import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

# Caminho absoluto da pasta static
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# ✅ Garante que a pasta static existe mesmo no Render
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, exist_ok=True)

app = FastAPI()

# Monta a rota static corretamente
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory="templates")

numeros_sorteados = []
quantidade_inicial = 50  # Pode alterar

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "quantidade_inicial": quantidade_inicial
    })

@app.post("/sortear", response_class=HTMLResponse)
async def sortear(request: Request):
    global numeros_sorteados
    numero = None

    if len(numeros_sorteados) < quantidade_inicial:
        numero = random.randint(1, quantidade_inicial)
        while numero in numeros_sorteados:
            numero = random.randint(1, quantidade_inicial)
        numeros_sorteados.append(numero)

    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numero_sorteado": numero,
        "numeros_sorteados": numeros_sorteados,
        "quantidade_inicial": quantidade_inicial
    })

@app.post("/resetar", response_class=HTMLResponse)
async def resetar(request: Request):
    global numeros_sorteados
    numeros_sorteados = []
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numero_sorteado": None,
        "numeros_sorteados": numeros_sorteados,
        "quantidade_inicial": quantidade_inicial
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sorteio_api:app", host="0.0.0.0", port=8000, reload=True)

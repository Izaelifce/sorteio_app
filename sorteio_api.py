
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

quantidade_inicial = 100  # Exemplo, ajuste conforme desejar
numeros_sorteados = []


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "numero_sorteado": None,
        "numeros_sorteados": numeros_sorteados
    })


# Endpoint de saúde (verificação se o servidor está online)
@app.get("/health")
async def health():
    return {"status": "ok"}


# Sorteio de número
@app.post("/sortear", response_class=HTMLResponse)
async def sortear(request: Request):
    global numeros_sorteados
    numero = None
    if len(numeros_sorteados) < quantidade_inicial:
        numero = random.randint(1, quantidade_inicial)
        while numero in numeros_sorteados:
            numero = random.randint(1, quantidade_inicial)
        numeros_sorteados.append(numero)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "numero_sorteado": numero,
        "numeros_sorteados": numeros_sorteados
    })


# Resetar sorteios
@app.post("/resetar", response_class=HTMLResponse)
async def resetar(request: Request):
    global numeros_sorteados
    numeros_sorteados = []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "numero_sorteado": None,
        "numeros_sorteados": numeros_sorteados
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sorteio_api:app", host="0.0.0.0", port=8000, reload=True)

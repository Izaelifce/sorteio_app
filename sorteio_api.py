ffrom fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

# Cria o app FastAPI
app = FastAPI()

# ✅ MONTA A PASTA STATIC (correção do erro NoMatchFound)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura o diretório de templates
templates = Jinja2Templates(directory="templates")

# Variáveis globais
numeros_sorteados = []
quantidade_inicial = 50  # Altere se quiser outra quantidade

# Página inicial
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numero_sorteado": None,
        "numeros_sorteados": numeros_sorteados,
        "quantidade_inicial": quantidade_inicial
    })

# Rota para sortear um número
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

# Rota para resetar os números sorteados
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

# Para rodar localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sorteio_api:app", host="0.0.0.0", port=8000, reload=True)

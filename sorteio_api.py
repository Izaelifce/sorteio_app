
import os
import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Diretórios base e static
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Criação do app FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory="templates")

# Variáveis globais do sorteio
numeros_sorteados = []
quantidade_inicial = 50  # Máximo número do sorteio

# Rota principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "numero_sorteado": None,
        "numeros_sorteados": numeros_sorteados
    })

# Rota de sorteio
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

# Rota para resetar o sorteio
@app.post("/resetar", response_class=HTMLResponse)
async def resetar(request: Request):
    global numeros_sorteados
    numeros_sorteados = []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "numero_sorteado": None,
        "numeros_sorteados": numeros_sorteados
    })

# 🔍 Rota de verificação de saúde (usada pelo Google e Render)
@app.get("/health")
async def health():
    return {"status": "ok"}

# 🔧 Debug opcional — lista arquivos em /static
@app.get("/debug-static")
def debug_static():
    if os.path.exists(STATIC_DIR):
        return {"arquivos_na_pasta_static": os.listdir(STATIC_DIR)}
    else:
        return {"erro": "Static directory não encontrado", "caminho_esperado": STATIC_DIR}

# Execução local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sorteio_api:app", host="0.0.0.0", port=8000, reload=True)

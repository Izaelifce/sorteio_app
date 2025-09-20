import os
import random
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Cria app
app = FastAPI()

# ✅ Usa caminhos absolutos para evitar erro no Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# ✅ Monta rota para arquivos estáticos (CSS, JS, imagens)
if not os.path.exists(STATIC_DIR):
    print(f"⚠️ Aviso: pasta static não encontrada em {STATIC_DIR}")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ✅ Configura templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Variáveis globais
numeros_sorteados = []
quantidade_inicial = 50  # Pode alterar

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Rota inicial - renderiza a página principal
    """
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "quantidade_inicial": quantidade_inicial,
        "numeros_sorteados": numeros_sorteados,
        "numero_sorteado": None
    })


@app.post("/sortear", response_class=HTMLResponse)
async def sortear(request: Request):
    """
    Sorteia um número e atualiza a lista de números sorteados
    """
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
    """
    Reseta a lista de números sorteados
    """
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
    uvicorn.run("sorteio_api:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)

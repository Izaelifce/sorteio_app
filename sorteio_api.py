from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import random
import uvicorn

if __name__ == "__main__":
    # Para servidores online, usar host 0.0.0.0 e porta do Render/Heroku
    uvicorn.run("sorteio_api:app", host="0.0.0.0", port=8000)


app = FastAPI()

# Serve os arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pasta de templates
templates = Jinja2Templates(directory="templates")

# ✅ Endpoint de Health Check
@app.get("/health")
def health_check():
    return {"status": "ok"}
# Variáveis de estado do sorteio
numeros_disponiveis = []
numeros_sorteados = []
numero_sorteado = None
quantidade_inicial = 0

# -----------------------------
# Função para abrir navegador
# -----------------------------

# -----------------------------
# Página principal
# -----------------------------




@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numeros_disponiveis": numeros_disponiveis,
        "numeros_sorteados": numeros_sorteados,
        "numero_sorteado": numero_sorteado,
        "quantidade_inicial": quantidade_inicial
    })

# -----------------------------
# Inicializa o sorteio
# -----------------------------
@app.post("/inicializar_web", response_class=HTMLResponse)
def inicializar_web(request: Request, quantidade: int = Form(...)):
    global numeros_disponiveis, numeros_sorteados, quantidade_inicial, numero_sorteado
    quantidade_inicial = quantidade
    numeros_disponiveis = list(range(1, quantidade_inicial + 1))
    numeros_sorteados = []
    numero_sorteado = None
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numeros_disponiveis": numeros_disponiveis,
        "numeros_sorteados": numeros_sorteados,
        "numero_sorteado": numero_sorteado,
        "quantidade_inicial": quantidade_inicial
    })

# -----------------------------
# Sorteia um número
# -----------------------------
@app.get("/sortear_web", response_class=HTMLResponse)
def sortear_web(request: Request):
    global numeros_disponiveis, numeros_sorteados, numero_sorteado
    if numeros_disponiveis:
        numero_sorteado = random.choice(numeros_disponiveis)
        numeros_disponiveis.remove(numero_sorteado)
        numeros_sorteados.append(numero_sorteado)
    else:
        numero_sorteado = "Todos sorteados!"
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numeros_disponiveis": numeros_disponiveis,
        "numeros_sorteados": numeros_sorteados,
        "numero_sorteado": numero_sorteado,
        "quantidade_inicial": quantidade_inicial
    })

# -----------------------------
# Reseta o sorteio
# -----------------------------
@app.get("/resetar_web", response_class=HTMLResponse)
def resetar_web(request: Request):
    global numeros_disponiveis, numeros_sorteados, numero_sorteado
    numeros_disponiveis = list(range(1, quantidade_inicial + 1))
    numeros_sorteados = []
    numero_sorteado = None
    return templates.TemplateResponse("index_igreja.html", {
        "request": request,
        "numeros_disponiveis": numeros_disponiveis,
        "numeros_sorteados": numeros_sorteados,
        "numero_sorteado": numero_sorteado,
        "quantidade_inicial": quantidade_inicial
    })

# -----------------------------
# Executa o servidor e abre o navegador

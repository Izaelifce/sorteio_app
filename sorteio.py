import tkinter as tk
import random

def sortear():
    nomes = entry.get().split(",")
    nomes = [nome.strip() for nome in nomes if nome.strip()]  # Remove espaços e nomes vazios
    if nomes:
        vencedor = random.choice(nomes)
        resultado_label.config(text=f"Vencedor: {vencedor}")
    else:
        resultado_label.config(text="Digite nomes separados por vírgula.")

app = tk.Tk()
app.title("Sorteio de Nomes")

label = tk.Label(app, text="Digite os nomes separados por vírgula:")
label.pack(pady=10)

entry = tk.Entry(app, width=50)
entry.pack(pady=5)

botao = tk.Button(app, text="Sortear", command=sortear)
botao.pack(pady=10)

resultado_label = tk.Label(app, text="")
resultado_label.pack(pady=10)

app.mainloop()

import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def check_url(url):
    try:
        response = requests.get(url)
        if "phishing" in response.text.lower():
            return "Possível phishing detectado!"
        else:
            return "URL segura."
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar URL: {e}"

def on_check_click():
    url = url_entry.get()
    result = check_url(url)
    messagebox.showinfo("Resultado", result)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Detector de Phishing")

tk.Label(root, text="Digite a URL para verificação:").pack(padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=10)

check_button = tk.Button(root, text="Verificar", command=on_check_click)
check_button.pack(padx=10, pady=10)

root.mainloop()

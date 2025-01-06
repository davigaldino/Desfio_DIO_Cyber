import tkinter as tk
import requests
import json


api_key = 'SUA_CHAVE_DA_API'  # Obtenha sua chave na plataforma Google Cloud

# Função para verificar a URL usando o Google Safe Browsing
def verificar_url():
    url = entry_url.get()  # Obtém a URL do campo de entrada
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # Adiciona https:// caso o usuário não tenha digitado
    
    # URL da API Google Safe Browsing
    safe_browsing_url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'
    
    # Dados da solicitação
    request_data = {
        "client": {
            "clientId": "your-client-id",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],  # Tipos de ameaça
            "platformTypes": ["WINDOWS"],  # Plataforma
            "threatEntryTypes": ["URL"],  # Tipo de entrada
            "threatEntries": [{"url": url}]
        }
    }

    try:
        # Enviando a solicitação
        response = requests.post(safe_browsing_url, json=request_data)
        response_data = response.json()  # Obtém a resposta em formato JSON
        
        # Verificando se a URL está na lista de ameaças
        if 'matches' in response_data:
            resultado.set(f"Atenção: URL suspeita! {url} está na lista de sites maliciosos.")
        else:
            resultado.set(f"URL segura: {url}")
    except Exception as e:
        resultado.set(f"Erro ao acessar a API: {str(e)}")

# Criando a interface gráfica com Tkinter
root = tk.Tk()
root.title("Verificador de URL")
root.geometry("450x250")

# Label para instrução
label_url = tk.Label(root, text="Digite a URL para verificação:")
label_url.pack(pady=10)

# Campo de entrada para a URL
entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=5)

# Botão para verificar a URL
btn_verificar = tk.Button(root, text="Verificar URL", command=verificar_url)
btn_verificar.pack(pady=10)

# Label para exibir o resultado da verificação
resultado = tk.StringVar()
label_resultado = tk.Label(root, textvariable=resultado, wraplength=400)
label_resultado.pack(pady=10)

# Inicia a interface gráfica
root.mainloop()

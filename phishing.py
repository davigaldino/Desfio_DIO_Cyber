import requests
from bs4 import BeautifulSoup

# Função para verificar se uma URL é phishing
def check_url(url):
    try:
        response = requests.get(url)
        if "phishing" in response.text.lower():
            return "Possível phishing detectado!"
        else:
            return "URL segura."
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar URL: {e}"

if __name__ == "__main__":
    url = input("Digite a URL para verificação: ")
    print(check_url(url))
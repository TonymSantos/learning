from bs4 import BeautifulSoup
import requests

def dicionario():
    palavra =input("Qual é a palavra? ")
    dic = requests.get(f"https://www.lexico.pt/{palavra}")
    if dic.status_code == 404:
        print("Palavra não encontrada.")

    soup = BeautifulSoup(dic.text, 'html.parser')
    resumo = soup.find("p", {"id":"significado"}).text

    print(resumo)

while True:
    dicionario()
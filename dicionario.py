
from tkinter import *
from bs4 import BeautifulSoup
import requests

def dicionario():
    palavra = palavra1.get()
    dic = requests.get(f"https://www.lexico.pt/{palavra}")
    if dic.status_code == 404:
        final.set("Palavra não encontrada.")

    soup = BeautifulSoup(dic.text, 'html.parser')
    resumo = soup.find("p", {"id":"significado"}).text

    final.set(resumo)

menu_inicial = Tk()
menu_inicial.title("Dicionário Online")

menu_inicial["bg"] = "light grey"
menu_inicial.geometry("500x250+200+200")
#menu_inicial.state("zoomed")
menu_inicial.resizable(True,True)
menu_inicial.iconbitmap("images/book.ico")

#Mensagem
msg1 = Label(menu_inicial,
             text="Qual é a palavra:",
             bg="#aaaaaa",
             fg="black",
             font="Arial 10 bold",
             bd=5,
             relief="raised")


#input
final = StringVar() 

msg1.grid(row= 0, sticky=N)
palavra1 = Entry(menu_inicial)
palavra1.grid(row= 0, column= 1)
cmd_palavra = Button(menu_inicial, text="Descobrir: ", command= dicionario)
cmd_palavra.grid(row= 2, column= 1, sticky=E)
resultado = Label(menu_inicial, 
                textvariable=final,
                justify=LEFT, 
                wraplength=500,
                bg="#aaaaaa",
                font="Arial 10")
resultado.grid(row= 3, column= 0, sticky=W)

menu_inicial.mainloop()
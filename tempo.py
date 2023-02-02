
from tkinter import *
from bs4 import BeautifulSoup
import requests


def tempo():

    api_key = "79804db17a955527ac66e95b6c33027b"

    user_input = palavra1.get()

    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

    if weather_data.json() ['cod'] == '404':
        final.set("Essa cidade não existe! ")
    else:
        weather = weather_data.json() ['weather'][0] ['main']
        temp = round(weather_data.json() ['main'] ['temp'])

        final.set(f"O tempo em {user_input} é de {weather}, e a temperatura é de {temp} graus")

menu_inicial = Tk()
menu_inicial.title("Dicionário Online")

menu_inicial["bg"] = "light grey"
menu_inicial.geometry("500x250+200+200")
#menu_inicial.state("zoomed")
menu_inicial.resizable(True,True)
menu_inicial.iconbitmap("images/tempo.ico")

#Mensagem
msg1 = Label(menu_inicial,
             text="Qual é a tua cidade:  ",
             bg="#aaaaaa",
             fg="black",
             font="Arial 10 bold",
             bd=5,
             relief="raised")

#input
final = StringVar() 

msg1.grid(row= 0, sticky=W)
palavra1 = Entry(menu_inicial)
palavra1.grid(row= 0, column= 1)
cmd_palavra = Button(menu_inicial, text="Descobrir: ", command= tempo)
cmd_palavra.grid(row= 2, column= 1, sticky=E)
resultado = Label(menu_inicial, 
                textvariable=final,
                justify=LEFT, 
                wraplength=500,
                bg="light blue",
                font="Arial 10")
resultado.grid(row= 3, column= 0)

menu_inicial.mainloop()
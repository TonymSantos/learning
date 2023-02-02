import requests

def tempo():

    api_key = "79804db17a955527ac66e95b6c33027b"

    user_input = input("Escolhe uma cidade: ")

    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

    if weather_data.json() ['cod'] == '404':
        print("Essa cidade não existe! ")
    else:
        weather = weather_data.json() ['weather'][0] ['main']
        temp = round(weather_data.json() ['main'] ['temp'])

        print(f"O tempo em {user_input} é de {weather}, e a temperatura é de {temp} graus")
while True:
    tempo()
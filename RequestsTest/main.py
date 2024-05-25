import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ea5b2b9bb0abcf57b55c2a1801d8be45'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


#Создание покемона
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

#Смена имени покемона
body_change_name = {
    "pokemon_id": response_create.json()['id'],
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

#Поймать покемона в покебол
body_catch = {
    "pokemon_id": response_create.json()['id']
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
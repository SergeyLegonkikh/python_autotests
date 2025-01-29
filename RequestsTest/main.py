import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '960f9a17244d5123d9951eabc9b59c35'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '960f9a17244d5123d9951eabc9b59c35'}
body_create = {
    "name": "Пупсень",
    "photo_id": 1,
    
}
body_put = {

    "pokemon_id": "203478",
    "name": "Плохиш",
    "photo_id": 2
}

body_pockebol = {
    "pokemon_id": "9"
}


response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_put) 
print(response)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response)


response = requests.put(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pockebol) 
print(response)
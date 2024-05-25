import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ea5b2b9bb0abcf57b55c2a1801d8be45'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4257'
TRAINER_NAME = 'Fyt'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

'''def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Бульбазавр'''

def test_trainer_name():
    response_trainer_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainer_name.json()['data'][0]['trainer_name'] == TRAINER_NAME

'''@pytest.mark.parametrize('key, value', [('name', 'Пикачу'), ('trainer_id', TRAINER_ID), ('id', '28328')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value'''
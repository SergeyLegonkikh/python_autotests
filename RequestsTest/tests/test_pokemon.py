import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '960f9a17244d5123d9951eabc9b59c35'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '960f9a17244d5123d9951eabc9b59c35'}
TRAINER_ID = 18117


def test_status_code():
  response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
  assert response.status_code == 200


def test_name_trainer():
      response_get = response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
      assert response_get.json()["data"][0]["trainer_name"] == 'Lovelas'


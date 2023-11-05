import requests

api_key = '4708ecfc-ffbc-4f03-811a-7b2b4cfd3ec3'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
import requests
import json

url = "http://127.0.0.1:5000/livros"
headers = {'Content-Type': 'application/json'}

# Definindo o novo livro
novo_livro = {
    'id': 5, 
    'titulo': 'Python POST TESTE', 
    'autor': 'Luciano XXX', 
    'ano_publicacao': 2020
}

# Fazendo a requisição POST
try:
    response = requests.post(url, headers=headers, data=json.dumps(novo_livro))
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
else:
    print(response.json())


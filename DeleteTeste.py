import requests

url = "http://127.0.0.1:5000/livros/1"

# Fazendo a requisição DELETE
response = requests.delete(url)

# Exibindo a resposta
print(response.json())
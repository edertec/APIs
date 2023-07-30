import requests
import json

url = "http://127.0.0.1:5000/livros/2"
headers = {'Content-Type': 'application/json'}

# Definindo os dados da atualização
atualizacao = {
    'ano_publicacao': 2025
}

# Fazendo a requisição PATCH
response = requests.patch(url, headers=headers, data=json.dumps(atualizacao))

# Exibindo a resposta
print(response.json())

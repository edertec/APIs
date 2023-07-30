import requests
import json

url = "http://127.0.0.1:5000/livros/1"
headers = {'Content-Type': 'application/json'}

# Definindo os novos dados do livro
livro_atualizado = {
    'titulo': 'Aprendendo Python, Edição Atualizada', 
    'ano_publicacao': 2023
}

# Fazendo a requisição PUT
response = requests.put(url, headers=headers, data=json.dumps(livro_atualizado))

# Exibindo a resposta
print(response.json())

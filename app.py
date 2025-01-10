import requests
import json

# URL do arquivo JSON no servidor
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

# Obtendo o arquivo JSON via HTTP
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    dados_json = response.json()  
    dados_restaurantes = {}

    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_do_restaurante] = []
        dados_restaurantes[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

    for nome_do_restaurante,dados_restaurantes in dados_restaurantes.items():
        nome_do_arquivo = f"{nome_do_restaurante}.json"
        with open(nome_do_arquivo, "w") as arquivo:
            json.dump(dados_restaurantes, arquivo, indent=4)
    
else:
    print(f"Erro ao acessar o arquivo: {response.status_code}")

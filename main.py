# Interação com Database (REST API)
import requests
import json

link = 'https://meuprojetojack-default-rtdb.firebaseio.com/'

# Criando uma venda Firebase (POST)
dados_vendas = {
    'cliente': 'Marcos',
    'produto': 'Calculadora',
    'valor': 40
}
requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados_vendas))
print(requisicao)
print(requisicao.text)

# Criando um produto Firebase (POST)
dados_produtos = {
    'nome': 'Calculadora',
    'quantidade': 452,
    'valor': 40
}
requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados_produtos))
print(requisicao)
print(requisicao.text)

# Editando de vendas no meu Banco de Dados (PATCH)
dados_vendas = {
    'cliente': 'Paulo',
}
requisicao = requests.patch(f'{link}/Vendas/-N2S038KNMFAVkW97t-_/.json', data=json.dumps(dados_vendas))
print(requisicao)
print(requisicao.text)

# Pegando uma venda especifico ou todas as vendas (GET)
req_id = None
requisicao = requests.get(f'{link}/Vendas/.json')
for v in requisicao.json():
    if requisicao.json()[v]["cliente"] == 'Lira':
        req_id = v


# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{req_id}/.json')
print(f'\033[1;32m {requisicao}')
print(f'\033[91m {requisicao.text}')

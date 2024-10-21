import requests
from datetime import datetime

urlBase = 'http://localhost:8500/apiGerenciamento/'

def createCategory(name, description):
    EndPoint = urlBase + 'categorias'
    categoria = {
        "nome": name,
        "descricao": description
    }
    try:
        response = requests.post(EndPoint, json=categoria)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

def createFornecedor(name, tel, email, endereco):
    EndPoint = urlBase + 'fornecedores'
    fornecedor = {
        "nome": name,
        "telefone": tel,
        "email": email,
        "endereco": endereco
    }
    try:
        response = requests.post(EndPoint, json=fornecedor)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

def createVendedor(name, username, email, senha, permissao):
    EndPoint = urlBase + 'vendedores'
    vendedor = {
        "nome": name,
        "username": username,
        "email": email,
        "senha": senha,
        "permissao": permissao
    }
    try:
        response = requests.post(EndPoint, json=vendedor)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

def createProdutos(id, name, description, price, quantity,  categoryID, supplierID):
    EndPoint = urlBase + 'produtos'
    produto = {
        "id": id,
        "nome": name,
        "descricao": description,
        "preco": price,
        "quantidade": quantity,
        "id_categoria": categoryID,
        "id_fornecedor": supplierID
    }
    try:
        response = requests.post(EndPoint, json=produto)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

def createVendas( qntd, id_produto, id_vendedor):
    EndPoint = urlBase + 'vendas'
    response = requests.get('http://worldclockapi.com/api/json/utc/now')
    data = response.json()
    current_time = data['currentDateTime']
    current_time = current_time.replace('Z', '+00:00')
    dt = datetime.fromisoformat(current_time)
    data_atual = dt.date()
    dataN = str(data_atual)

    venda = {
        "data_venda": dataN,
        "quantidade_vendida": qntd,
        "id_produto": id_produto,
        "id_vendedor": id_vendedor
    }
    try:
        response = requests.post(EndPoint, json=venda)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e


def createEntradas(qntd, id_produto, id_Fornecedor, valor):
    EndPoint = urlBase + 'entradas'
    response = requests.get('http://worldclockapi.com/api/json/utc/now')

    data = response.json()
    current_time = data['currentDateTime']
    current_time = current_time.replace('Z', '+00:00')
    dt = datetime.fromisoformat(current_time)
    data_atual = dt.date()
    dataN = str(data_atual)
    entrada = {
        "data_entrada": dataN,
        "quantidade_entrada": qntd,
        "preco": valor,
        "id_produto": id_produto,
        "id_fornecedor": id_Fornecedor
    }
    try:
        response = requests.post(EndPoint, json=entrada)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

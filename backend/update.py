import requests
import backend.read as r

urlBase = 'http://localhost:8500/apiGerenciamento/'
    
def updateProductQntd(id, quantity):
    EndPoint = urlBase + f'produtos/{id}'
    result = r.readProdutos()
    produto = {
        "quantidade": quantity,
    }
    try:
        response = requests.put(EndPoint, json=produto)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f'erro {e}')
        return e


def updateCategory(id, name, description):
    EndPoint = urlBase + f'categorias/{id}'
    categoria = {
        "nome": name,
        "descricao": description
    }
    try:
        response = requests.put(EndPoint, json=categoria)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

def updateFornecedor(id, name, telefone, email, endereco):
    EndPoint = urlBase + f'fornecedores/{id}'
    fornecedor = {
        "nome": name,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    try:
        response = requests.put(EndPoint, json=fornecedor)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return e

def updateProdutos(id, name, description, price, quantity, categoryID, supplierID):
    EndPoint = urlBase + f'produtos/{id}'
    produto = {
        "nome": name,
        "descricao": description,
        "preco": price,
        "quantidade": quantity,
        "id_categoria": categoryID,
        "id_fornecedor": supplierID
    }
    try:
        response = requests.put(EndPoint, json=produto)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f'erro {e}')
        return e

def updateQtdProdutos(id, qtd):
    EndPoint = urlBase + f'produtosEX/{id}'
    produto = {
        "quantidade_venda_excluida": qtd
    }
    try:
        response = requests.put(EndPoint, json=produto)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f'erro {e}')
        return e
    
def updateVendedores(id, name, username, email, senha, permissao):
    EndPoint = urlBase + f'vendedores/{id}'
    vendedor = {
        "nome": name,
        "username": username,
        "email": email,
        "senha": senha,
        "permissao": permissao
    }
    try:
        response = requests.put(EndPoint, json=vendedor)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f'erro {e}')
        return e


def updateVendas(id, qtd, cdP, cdV):
    EndPoint = urlBase + f'vendas/{id}'
    venda = {
        "quantidade_vendida": qtd
    }
    try:
        response = requests.put(EndPoint, json=venda)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f'erro {e}')
        return e
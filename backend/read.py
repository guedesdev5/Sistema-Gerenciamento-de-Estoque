import requests

urlBase = 'http://localhost:8500/apiGerenciamento/'

def readProdutos ():
    EndPoint = urlBase + 'produtos'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e
            

def readProdutos (id):
    EndPoint = urlBase + f'produtos?id={id}'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e

def readProdutos ():
    EndPoint = urlBase + 'produtos'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e

def readCategoria ():
    EndPoint = urlBase + 'categorias'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e

    
def readVender ():
    EndPoint = urlBase + 'vendedores'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e
    
def readFornecedor ():
    EndPoint = urlBase + 'fornecedores'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e
    
def readVendas ():
    EndPoint = urlBase + 'vendas'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e
import requests

urlBase = 'http://localhost:8500/apiGerenciamento/'

def deleteCategoria(id):
    EndPoint = urlBase + f'categorias/{id}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e
    
def deleetFornecedor(id):
    EndPoint = urlBase + f'fornecedores/{id}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e
    
def deleteProdutos(id):
    EndPoint = urlBase + f'produtos/{id}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e

def deleetVendedores(id):
    EndPoint = urlBase + f'vendedores/{id}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e
    
def deleteVendas(id):
    print(f'testando valor do id {id}')
    EndPoint = urlBase + f'vendas/{id}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e

def deleteEntradas(idE, id_produto, qntd):
    EndPoint = urlBase + f'entradas/{idE}/{id_produto}/{qntd}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e
import requests

urlBase = 'https://apiigerenciamento.onrender.com/apiGerenciamento/'

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
    
def deleteVendas(id, id_produto, qntd):

    EndPoint = urlBase + f'vendas/{id}/{id_produto}/{qntd}'
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
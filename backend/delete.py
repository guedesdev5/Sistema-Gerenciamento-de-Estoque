import requests

urlBase = 'http://localhost:8500/apiGerenciamento/'

def deleteCategoria(id):
    EndPoint = urlBase + f'categorias/{id}'
    try:
        response = requests.delete(EndPoint)
        return response.json()
    except Exception as e:
        return e
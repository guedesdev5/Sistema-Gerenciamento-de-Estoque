import mysql.connector
import requests

urlBase = 'http://localhost:8500/apiGerenciamento/'

def getConnection():
    global database
    database = mysql.connector.Connect(host="localhost", database="sistema_geranciamento", user="root", password="pietro29012007")

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
    getConnection()
    if database.is_connected():
        try:
             cursor = database.cursor() 
             cursor.execute(f'''INSERT into vendedores 
             (nome, username, email, senha, permissao) 
             values 
             ("{name}", "{username}", "{email}", "{senha}", {permissao})''')
             database.commit()
             return 1
        except Exception as error:
            return error
    return 2

def createProdutos(id, name, description, price, quantity, categoryID, supplierID):
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
    getConnection()
    if database.is_connected():
        try:
             cursor = database.cursor() 
             cursor.execute(f'''INSERT into vendas 
             ( quantidade_vendida, id_produto, id_vendedor) 
             values 
             ( {qntd}, {id_produto}, {id_vendedor})''')
             database.commit()
             return 1
        except Exception as error:
            return error
    return 2
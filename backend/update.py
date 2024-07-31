import mysql.connector
import requests

urlBase = 'http://localhost:8500/apiGerenciamento/'

def getConnection():
    global database
    database = mysql.connector.Connect(host="localhost", database="sistema_geranciamento", user="root", password="pietro29012007")

def update(id, name, description, price, quantity, categoryID, supplierID):
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(f'''UPDATE produtos set nome = "{name}", descricao = "{description}", 
            preco = {price}, quantidade = {quantity}, id_categoria = {categoryID}, id_fornecedor = 
            {supplierID} WHERE id = {id}''')
            database.commit()
            return 1
        except:
            return 0
    else:
        return 2
    
def updateProductQntd(id, quantity):
    EndPoint = urlBase + f'produtos/{id}'
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
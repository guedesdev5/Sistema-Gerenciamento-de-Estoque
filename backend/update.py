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
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(f'UPDATE produtos set quantidade = quantidade - {quantity} WHERE id = {id}')
            database.commit()
        except Exception as e:
            print(e)

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

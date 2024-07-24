import mysql.connector
import requests

urlBase = 'http://localhost:8500/apiGerenciamento/'

def getConnection():
    global database
    database = mysql.connector.Connect(host="localhost", database="sistema_geranciamento", user="root", password="pietro29012007")

def readProdutos ():
    EndPoint = urlBase + 'produtos'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e
        return 2

def readAcorderID (id):
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(f'SELECT * from produtos WHERE id = {id}')
            results = cursor.fetchall()
            return results
        except:
            return 0
    else:
        return 2
            

def readCategoria ():
    EndPoint = urlBase + 'categorias'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e

    
def readVender ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute('SELECT * from vendedores')
            results = cursor.fetchall()
                    
            return results
        except Exception as e:
            return e
    else:
        return 2
    
def readFornecedor ():
    EndPoint = urlBase + 'fornecedores'
    try:
        response = requests.get(EndPoint)
        return response.json()
    except Exception as e:
        return e
    
def readVendas ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute('SELECT * from vendas')
            results = cursor.fetchall()
                    
            return results
        except Exception as e:
            return e
    else:
        return 2
    
def readIdCategory ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(' SELECT id FROM categorias')
            results = cursor.fetchall()

# Retornar a lista de resultados
            return results
        except Exception as e:
            return e
    else:
        return 2
    
def readIdFornecedores ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(' SELECT id FROM fornecedores')
            results = cursor.fetchall()
            
# Retornar a lista de resultados
            return results
        except Exception as e:
            return e
    else:
        return 2

def readIdvendedor ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(' SELECT id FROM vendedores')
            results = cursor.fetchall()
            
# Retornar a lista de resultados
            return results
        except Exception as e:
            return e
    else:
        return 2
    
def readIdprodutos ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(' SELECT id FROM produtos')
            results = cursor.fetchall()
            
# Retornar a lista de resultados
            return results
        except Exception as e:
            return e
    else:
        return 2
   

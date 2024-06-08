import mysql.connector

def getConnection():
    global database
    database = mysql.connector.Connect(host="localhost", database="sistema_geranciamento", user="root", password="pietro29012007")

def readProdutos ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute('SELECT * from produtos')
            results = cursor.fetchall()
                    
            return results
        except Exception as e:
            return e
    else:
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
            
def delete(id):
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(f'DELETE from produtos WHERE id = {id}')
            database.commit()
            return 1
        except:
            return 0
    else:
        return 2
    
def readCategory ():
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute('SELECT * from categorias')
            results = cursor.fetchall()
                    
            return results
        except Exception as e:
            return e
    else:
        return 2
    
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
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute('SELECT * from fornecedores')
            results = cursor.fetchall()
                    
            return results
        except Exception as e:
            return e
    else:
        return 2
    
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
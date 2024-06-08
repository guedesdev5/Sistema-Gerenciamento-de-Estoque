import mysql.connector

def getConnection():
    global database
    database = mysql.connector.Connect(host="localhost", database="sistema_geranciamento", user="root", password="pietro29012007")

def createCategory(name, description):
    getConnection()
    if database.is_connected():
        try:
             cursor = database.cursor() 
             cursor.execute(f'''INSERT into categorias 
             (nome, descricao) 
             values 
             ("{name}", "{description}")''')
             database.commit()
             return 1
        except Exception as error:
            return error
    return 2

def createFornecedor(name, tel, email, endereco):
    getConnection()
    if database.is_connected():
        try:
             cursor = database.cursor() 
             cursor.execute(f'''INSERT into fornecedores 
             (nome, telefone, email, endereco) 
             values 
             ("{name}", "{tel}", "{email}", "{endereco}")''')
             database.commit()
             return 1
        except Exception as error:
            return error
    return 2

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
    getConnection()
    if database.is_connected():
        try:
             cursor = database.cursor() 
             cursor.execute(f'''INSERT into produtos 
             (id, nome, descricao, preco, quantidade, id_categoria, id_fornecedor) 
             values 
             ({id}, "{name}", "{description}", {price}, {quantity}, {categoryID}, {supplierID})''')
             database.commit()
             print('deu')
             return 1
        except Exception as error:
            return error
    return 2

def createVendas(data, qntd, id_produto, id_vendedor):
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
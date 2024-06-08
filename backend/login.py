import mysql.connector

def getConnection():
    global database
    database = mysql.connector.Connect(host="localhost", database="loja", user="root", password="pietro29012007")

def getLogin(username, password):
    getConnection()
    if database.is_connected():
        try:
            cursor = database.cursor()
            cursor.execute(f'SELECT senha from vendedores WHERE username = "{username}"')
            result = cursor.fetchall()
            if len(result) > 0:
                if result[0][0] == password:
                    return 1
                else:
                    return 3
            else:
                return 0
        except Exception as e:
            return e
    else:
        return 2


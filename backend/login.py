import requests

def login(username, senha):
    url = f'https://apigerenciamento.onrender.com/apiGerenciamento/vendedores?username={username}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
       
        for usuario in dados['data']:
            if usuario['username'] == username and usuario['senha'] == senha:
                return usuario['permissao']
        return 9
    else:
        print(f'Erro: {response.status_code}')
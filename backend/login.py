import requests

def login(username, senha):
    url = f'http://localhost:8500/apiGerenciamento/vendedores?username={username}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados['data'][0]['username'] == username and dados['data'][0]['senha'] == senha:
            return dados['data'][0]['permissao']
        else:
            return 9
    else:
        print(f'Erro: {response.status_code}')
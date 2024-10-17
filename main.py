from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

import backend.login as l
import backend.read as r
import backend.create as c
import backend.update as u
import backend.delete as d
import backend.dashboard as dash

app = Flask(__name__)
app.secret_key = 'abcdohdohfhef32833'

@app.route("/")
def home():
    return render_template("login.html")
    
@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    login = l.login(username, password)
    if login != 9:
        readBD = r.readProdutos()
        readIdCategory = r.readCategoria()
        readIdFornecedores = r.readFornecedor()
        idCategorias = [item['id'] for item in readIdCategory['data']]
        idFornecedores = [item['id'] for item in readIdFornecedores['data']]
        print(idCategorias)
        print(idFornecedores)
        if login == 1:
            app.config['PERMISSION_USER'] = True
        else:
            app.config['PERMISSION_USER'] = False
        
        flash('Login efetuado com sucesso!', 'success')
        return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        flash('Problema ao efetuar login!', 'error')
        return render_template("login.html")


@app.route("/produtos", methods=['POST'])
def produtos():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    category_id = request.form.get('category_id')
    fornecedor_id = request.form.get('fornecedor_id')
    response = c.createProdutos(int(id), name, description, float(price), int(quantity), int(category_id), int(fornecedor_id))
    readBD = r.readProdutos()
    readIdCategory = r.readCategoria()
    readIdFornecedores = r.readFornecedor()
    idCategorias = readIdCategory['data']
    idFornecedores = readIdFornecedores['data']
    
    if response['status'] == 0:
        flash('Produto cadastrado com sucesso!', 'success')
        return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        print(response['error']['code'])
        if response['error']['code'] == 'P2002':
            flash('Código inserido já existe!!', 'error')
            return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))
        flash('Problema ao cadastrar o produto!', 'error')
        return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/categorias", methods=['POST'])
def categoriaspost():
    name = request.form.get('name')
    description = request.form.get('description')
    response = c.createCategory(name, description)
    readBD = r.readCategoria()
    if response['status'] == 0:
        flash('Categoria cadastrada com sucesso!', 'success')
        return render_template("categorias.html", lista = readBD['data'])
    else:
        flash('Problema ao cadastrar a categoria!', 'error')
        return render_template("categorias.html", lista = readBD['data'])
    
@app.route('/editar/categoria', methods=['POST'])
def editarCategoria():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    response = u.updateCategory(id, nome, descricao)
    if response['status'] == 0:
        flash('Edição realizada com sucesso!', 'success')
        return redirect(url_for('categorias'))
    else:
        flash('Problema ao realizar a edição!', 'error')
        return redirect(url_for('categorias'))
    
@app.route('/excluir/categoria', methods=['post'])
def excluirCategoria():
    id = request.form['id'] 
    response = d.deleteCategoria(id)
    if response['status'] == 0:
        flash('Exclusão realizada com sucesso!', 'success')
        return redirect(url_for('categorias'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return redirect(url_for('categorias'))
    
@app.route("/fornecedores", methods=['POST'])
def fornecedorespost():
    name = request.form.get('name')
    tel = request.form.get('tel')
    email = request.form.get('email')
    endereco = request.form.get('endereco')
    response = c.createFornecedor(name, tel, email, endereco)
    readBD = r.readFornecedor()
    if response['status'] == 0:
        flash('Cadastro realizado com sucesso!', 'success')
        return render_template("fornecedores.html", lista = readBD['data'])
    else:
        flash('Problema ao realizar o cadastro!', 'error')
        return render_template("fornecedores.html", lista = readBD['data'])
    
@app.route('/editar/fornecedores', methods=['POST'])
def editarFornecedor():
    id = request.form['id']
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    endereco = request.form['endereco']
    response = u.updateFornecedor(id, nome, telefone, email, endereco)
    if response['status'] == 0:
        flash('Edição realizada com sucesso!', 'success')
        return redirect(url_for('fornecedores'))
    else:
        flash('Problema ao realizar a edição!', 'error')
        return redirect(url_for('fornecedores'))
    
@app.route('/excluir/fornecedores', methods=['post'])
def excluirFornecedor():
    id = request.form['id'] 
    response = d.deleetFornecedor(id)
    if response['status'] == 0:
        flash('Exclusão realizada com sucesso!', 'success')
        return redirect(url_for('fornecedores'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return redirect(url_for('fornecedores'))

@app.route('/editar/produtos', methods=['POST'])
def editarProdutos():
    id = request.form.get('id')
    name = request.form.get('nome')
    description = request.form.get('descricao')
    price = request.form.get('preco')
    quantity = request.form.get('quantidade')
    category_id = request.form.get('idCategoria')
    fornecedor_id = request.form.get('idFornecedor')
    response = u.updateProdutos(int(id), name, description, float(price), int(quantity))
    print(response)
    if response['status'] == 0:
        flash('Edição realizada com sucesso!', 'success')
        return redirect(url_for('homepage'))
    else:
        flash('Problema ao realizar a edição!', 'error')
        return redirect(url_for('homepage'))
    
@app.route('/excluir/produtos', methods=['post'])
def excluirProdutos():
    id = request.form['id'] 
    response = d.deleteProdutos(id)
    if response['status'] == 0:
        flash('Exclusão realizada com sucesso!', 'success')
        return redirect(url_for('homepage'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return redirect(url_for('homepage'))

@app.route("/vendedores", methods=['POST'])
def vendedorespost():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    senha = request.form.get('password')
    permissao = request.form.get('permission')
    result = c.createVendedor(name, username, email, senha, int(permissao))
    readBD = r.readVender()
    for user in readBD['data']:
        if user['permissao'] == 1:
            user['permissao'] = "Administrador"
        else:
            user['permissao'] = "Agente"
    if result['status'] == 0:
        flash('Cadastro realizado com sucesso!', 'success')
        return render_template("vendedores.html", lista = readBD['data'])
    else:
        flash('Problema ao realizar o cadastro!', 'error')
        return render_template("vendedores.html", lista = readBD['data'])
    
@app.route('/editar/vendedores', methods=['POST'])
def editarVendedores():
    id = request.form['id'] 
    name = request.form.get('nome')
    username = request.form.get('username')
    email = request.form.get('email')
    senha = request.form.get('senha')
    permissao = request.form.get('permissao')
    response = u.updateVendedores(int(id), name, username, email, senha, int(permissao))
    print(response)
    if response['status'] == 0:
        flash('Edição realizada com sucesso!', 'sucess')
        return redirect(url_for('vendedores'))
    else:
        flash('Problema ao realizar a edição!', 'error')
        return redirect(url_for('vendedores'))
    
@app.route('/excluir/vendedores', methods=['post'])
def excluirVendedoress():
    id = request.form['id'] 
    response = d.deleetVendedores(id)
    if response['status'] == 0:
        flash('Exculsão realizada com sucesso!', 'sucess')
        return redirect(url_for('vendedores'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return redirect(url_for('vendedores'))
    
@app.route("/vendas", methods=['POST'])
def vendaspost():
    qntd = request.form.get('qntd')
    cd_produto = request.form.get('cod')
    cd_vendedor = request.form.get('codv')
    response = r.readProdutosID(cd_produto)
    readIdVendedor = r.readVender()
    readBD = r.readVendas()
    readIdProdutos = r.readProdutos()
    idvendedor = readIdVendedor['data']
    idProdutos = readIdProdutos['data']
    if int(response['data'][0]['quantidade']) - int(qntd) < 0:
        flash('Impossível efetuar venda! Estoque de produtos  insuficiete', 'error')
        return render_template("vendas.html", lista = readBD['data'], readIdVendedor = idvendedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    result = c.createVendas( int(qntd), int(cd_produto), int(cd_vendedor))   
    if result['status'] == 0:
        readBD = r.readVendas()
        flash('Cadastro realizado com sucesso!', 'sucess')
        return render_template("vendas.html", lista = readBD['data'], readIdVendedor = idvendedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        flash('Problema ao realizar o cadastro!', 'error')
        return render_template("vendas.html", lista = readBD['data'], readIdVendedor = idvendedor, readIdProdutos = idProdutos, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/editar/vendas", methods=['POST'])
def vendasupdate():
    id = request.form.get('IDVenda')
    qntd = request.form.get('quantidadeVendas')
    cd_produto = request.form.get('idProduto')
    cd_vendedor = request.form.get('codVendedor')
    result = u.updateVendas( int(id), int(qntd), int(cd_produto))
    if result['status'] == 0:
        flash('Edição realizada com sucesso!', 'sucess')
        return redirect(url_for('vendas'))
    else:
        flash('Problema ao realizar a edição!', 'error')
        return redirect(url_for('vendas'))
    
@app.route('/excluir/vendas', methods=['post'])
def excluirVendas():
    id = request.form.get('vendasIdExclusao')
    id_produto = request.form.get('codProdutoEx')
    qntd = request.form.get('quantidadeVendasEX')
    print(id)
    print(id_produto)
    print(qntd)
    response = d.deleteVendas(id, id_produto, qntd)
    print(response)
    if response['status'] == 0:
        flash('Exclusão realizada com sucesso!', 'sucess')
        return redirect(url_for('vendas'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return redirect(url_for('vendas'))


@app.route("/entradas", methods=['POST'])
def entradaspost():
    qntd = request.form.get('qntd')
    cd_produto = request.form.get('codP')
    cd_fornecedor = request.form.get('cod')
    valor_entrada = request.form.get('valor')
    result = c.createEntradas( int(qntd), int(cd_produto), int(cd_fornecedor), int(valor_entrada))
    readBD = r.readEntradas()
    readFornecedor = r.readFornecedor()
    readIdProdutos = r.readProdutos()
    idFornecedor = readFornecedor['data']
    idProdutos = readIdProdutos['data']
    if result['status'] == 0:
        flash('Cadastro realizado com sucesso!', 'sucess')
        return render_template("entradas.html", lista = readBD['data'], readIdFornecedor = idFornecedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return render_template("entradas.html", lista = readBD['data'], readIdFornecedor = idFornecedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/editar/entradas", methods=['POST'])
def entradasupdate():
    id = request.form.get('ID')
    qntd = request.form.get('quantidadeEntrada')
    cd_produto = request.form.get('idProduto')
    preco = request.form.get('precoEntrada')
    response = u.updateEntradas( int(id), int(qntd), int(cd_produto), int(preco))
    if response['status'] == 0:
        flash('Edição realizada com sucesso!', 'sucess')
        return redirect(url_for('entradas'))
    else:
        flash('Problema ao realizar a edição!', 'error')
        return redirect(url_for('entradas'))

@app.route('/excluir/entradas', methods=['post'])
def excluirEntradas():
    id = request.form.get('idEntrada')
    id_produto = request.form.get('ProdutoIdExclusao')
    qntd = request.form.get('quantidadeEntradasEX')

    response = d.deleteEntradas(int(id), int(id_produto), int(qntd))
    if response['status'] == 0:
        flash('Exclusão realizada com sucesso!', 'sucess')
        return redirect(url_for('entradas'))
    else:
        flash('Problema ao realizar a exclusão!', 'error')
        return redirect(url_for('entradas'))

@app.route("/vendedores")
def vendedores():
    readBD = r.readVender()
    for user in readBD['data']:
        if user['permissao'] == 1:
            user['permissao'] = "Administrador"
        else:
            user['permissao'] = "Agente"
    return render_template("vendedores.html", lista = readBD['data'])

@app.route("/homepage")
def homepage():
    readBD = r.readProdutos()
    readIdCategory = r.readCategoria()
    readIdFornecedores = r.readFornecedor()
    idCategorias = readIdCategory['data']
    idFornecedores = readIdFornecedores['data']
    return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))
  

@app.route("/categorias")
def categorias():
    readBD = r.readCategoria()
    return render_template("categorias.html",  lista = readBD['data'])

@app.route("/vendas")
def vendas():
    readBD = r.readVendas()
    
    readIdVendedor = r.readVender()
    readIdProdutos = r.readProdutos()
    idvendedor = readIdVendedor['data']
    idProdutos = readIdProdutos['data']
    return render_template("vendas.html", lista = readBD['data'], readIdVendedor = idvendedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/fornecedores")
def fornecedores():
    readBD = r.readFornecedor()
    return render_template("fornecedores.html",  lista = readBD['data'])

@app.route("/entradas")
def entradas():
    readBD = r.readEntradas()
    readFornecedor = r.readFornecedor()
    readIdProdutos = r.readProdutos()
    idFornecedor = readFornecedor['data']
    idProdutos = readIdProdutos['data']
    return render_template("entradas.html", lista = readBD['data'], readIdFornecedor = idFornecedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    
@app.route("/dashboard")
def dashboard():
    dataAtual = dash.pegarDataAtual()
    dados_entrada = r.readEntradas()
    dataFiltradosEntrada = dash.filtrarDados(dados_entrada, dataAtual, 'entrada')
    dados_venda = r.readVendas()
    dadosFiltradosVendas= dash.filtrarDados(dados_venda, dataAtual, 'venda')
    df_relacao = dash.unir_dados(dados_entrada['data'], dados_venda['data'])  
    produtos = r.readProdutos()
    categorias = r.readCategoria()

    graph = dash.criar_dashboard(df_relacao)
    lucro_por_categoria = dash.calcularLucro(dados_entrada, dados_venda, produtos, categorias)
    mes_atual = dash.getStringMes(dataAtual)
    pie_graph = dash.criarDashboardLucro(list(lucro_por_categoria.keys()), list(lucro_por_categoria.values()))
    return render_template('dashboard.html', mes=mes_atual, graph=graph, pie_graph=pie_graph, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/FiltrarDashboard", methods=['post'])
def FiltrarDashboard():
    date = request.form.get('date-picker')
    dados_entrada = r.readEntradas()
    dadosFiltradosEntrada = dash.filtrarDados(dados_entrada, date, 'entrada')
    dados_venda = r.readVendas()
    dadosFiltradosVendas= dash.filtrarDados(dados_venda, date, 'venda')
    produtos = r.readProdutos()
    categorias = r.readCategoria()
    mes_atual = dash.getStringMes(date)
    if dadosFiltradosEntrada == 1 or dadosFiltradosVendas == 1:
        print('Vai corinthians')
        flash('Não há dados suficientes no mês escolhido!', 'error')
        return render_template('dashboard.html', mes=mes_atual, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    
    lucro_por_categoria = dash.calcularLucro(dados_entrada, dados_venda, produtos, categorias)
    df_relacao = dash.unir_dados(dadosFiltradosEntrada, dadosFiltradosVendas)  
    graph = dash.criar_dashboard(df_relacao)
    pie_graph = dash.criarDashboardLucro(list(lucro_por_categoria.keys()), list(lucro_por_categoria.values()))

    return render_template('dashboard.html', mes=mes_atual, graph=graph, pie_graph=pie_graph, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))



@app.route("/login")
def loginO():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port = 1404, debug = True)

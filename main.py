from flask import Flask, render_template, request, flash, redirect, url_for

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
        
        return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    else:
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
        return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        return render_template("homepage.html", lista = readBD['data'], idCategory = idCategorias, readIdFornecedores = idFornecedores, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/categorias", methods=['POST'])
def categoriaspost():
    name = request.form.get('name')
    description = request.form.get('description')
    response = c.createCategory(name, description)
    readBD = r.readCategoria()
    if response['status'] == 0:
        return render_template("categorias.html", lista = readBD['data'])
    else:
        return render_template("categorias.html", lista = readBD['data'])
    
@app.route('/editar/categoria', methods=['POST'])
def editarCategoria():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    response = u.updateCategory(id, nome, descricao)
    if response['status'] == 0:
        return redirect(url_for('categorias'))
    else:
        return redirect(url_for('categorias'))
    
@app.route('/excluir/categoria', methods=['post'])
def excluirCategoria():
    id = request.form['id'] 
    response = d.deleteCategoria(id)
    if response['status'] == 0:
        return redirect(url_for('categorias'))
    else:
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
        return render_template("fornecedores.html", lista = readBD['data'])
    else:
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
        return redirect(url_for('fornecedores'))
    else:
        return redirect(url_for('fornecedores'))
    
@app.route('/excluir/fornecedores', methods=['post'])
def excluirFornecedor():
    id = request.form['id'] 
    response = d.deleetFornecedor(id)
    if response['status'] == 0:
        return redirect(url_for('fornecedores'))
    else:
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
    response = u.updateProdutos(int(id), name, description, float(price), int(quantity), int(category_id), int(fornecedor_id))
    print(response)
    if response['status'] == 0:
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))
    
@app.route('/excluir/produtos', methods=['post'])
def excluirProdutos():
    id = request.form['id'] 
    response = d.deleteProdutos(id)
    if response['status'] == 0:
        return redirect(url_for('homepage'))
    else:
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
    if result == 1:
        return render_template("vendedores.html", lista = readBD['data'])
    else:
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
        return redirect(url_for('vendedores'))
    else:
        return redirect(url_for('vendedores'))
    
@app.route('/excluir/vendedores', methods=['post'])
def excluirVendedoress():
    id = request.form['id'] 
    response = d.deleetVendedores(id)
    if response['status'] == 0:
        return redirect(url_for('vendedores'))
    else:
        return redirect(url_for('vendedores'))
    
@app.route("/vendas", methods=['POST'])
def vendaspost():
    qntd = request.form.get('qntd')
    cd_produto = request.form.get('cod')
    cd_vendedor = request.form.get('codv')
    result = c.createVendas( int(qntd), int(cd_produto), int(cd_vendedor))
    responseProduto = r.readProdutosID(int(cd_produto))
    qtd_atual = int(responseProduto['data'][0]['quantidade'])
    qtd_validada = qtd_atual - int(qntd)
    readBD = r.readVendas()
    readIdVendedor = r.readVender()
    readIdProdutos = r.readProdutos()
    idvendedor = readIdVendedor['data']
    idProdutos = readIdProdutos['data']
    u.updateProductQntd(cd_produto, int(qtd_validada))
    if result == 1:
        return render_template("vendas.html", lista = readBD['data'], readIdVendedor = idvendedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        return render_template("vendas.html", lista = readBD['data'], readIdVendedor = idvendedor, readIdProdutos = idProdutos, permissionUser = app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/editar/vendas", methods=['POST'])
def vendasupdate():
    id = request.form.get('IDVenda')
    qntd = request.form.get('quantidadeVendas')
    cd_produto = request.form.get('codProduto')
    cd_vendedor = request.form.get('codVendedor')
    qtd_antiga = r.readVendasID(int(id))
    qtd_produto = r.readProdutosID(int(cd_produto))
    print(qtd_antiga)
    print(qtd_produto)
    qtd_validada = qtd_antiga['data'][0]['quantidade_vendida'] + qtd_produto['data'][0]['quantidade'] 
    qtd_atual = int(qtd_validada) - int(qntd)
    result = u.updateVendas( int(id), int(qntd), int(cd_produto), int(cd_vendedor))
    readIdVendedor = r.readVender()
    readIdProdutos = r.readProdutos()
    u.updateProductQntd(cd_produto, qtd_atual)
    if result == 1:
         return redirect(url_for('vendas'))
    else:
         return redirect(url_for('vendas'))
    
@app.route('/excluir/vendas', methods=['post'])
def excluirVendas():
    id = request.form.get('vendasIdExclusao')
    id_produto = request.form.get('codProdutoEx')
    qntd = request.form.get('quantidadeVendasEX')
    response = d.deleteVendas(id)
    print(id_produto)
    print(qntd)
    ajusta_quantidade = u.updateQtdProdutos(id_produto, qntd)
    print(f'tajusat   {ajusta_quantidade}')
    if response['status'] == 0:
        return redirect(url_for('vendas'))
    else:
        return redirect(url_for('vendas'))


@app.route("/entradas", methods=['POST'])
def entradaspost():
    qntd = request.form.get('qntd')
    cd_produto = request.form.get('codP')
    cd_fornecedor = request.form.get('cod')
    print(cd_fornecedor)
    result = c.createEntradas( int(qntd), int(cd_produto), int(cd_fornecedor))
    readBD = r.readEntradas()
    readFornecedor = r.readFornecedor()
    readIdProdutos = r.readProdutos()
    idFornecedor = readFornecedor['data']
    idProdutos = readIdProdutos['data']
    if result == 1:
        return render_template("entradas.html", lista = readBD['data'], readIdFornecedor = idFornecedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))
    else:
        return render_template("entradas.html", lista = readBD['data'], readIdFornecedor = idFornecedor, readIdProdutos = idProdutos, permissionUser =  app.config.get('PERMISSION_USER', 'default_permission'))

@app.route("/editar/entradas", methods=['POST'])
def entradasupdate():
    id = request.form.get('ID')
    qntd = request.form.get('quantidadeEntrada')
    cd_produto = request.form.get('idProduto')
    response = u.updateEntradas( int(id), int(qntd), int(cd_produto))
    if response == 1:
         return redirect(url_for('entradas'))
    else:
         return redirect(url_for('entradas'))

@app.route('/excluir/entradas', methods=['post'])
def excluirEntradas():
    id = request.form.get('idEntrada')
    id_produto = request.form.get('ProdutoIdExclusao')
    qntd = request.form.get('quantidadeEntradasEX')
    print(id)
    print(id_produto)
    print(qntd)
    response = d.deleteEntradas(int(id), int(id_produto), int(qntd))
    if response['status'] == 0:
        return redirect(url_for('entradas'))
    else:
        return redirect(url_for('entradas'))

@app.route("/vendedores")
def vendedores():
    readBD = r.readVender()
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
    vendas = {
        "meses": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
        "valores": [500, 700, 800, 600, 900, 1000]
    }
    entradas = {
        "meses": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
        "valores": [300, 400, 350, 500, 600, 550]
    }
    graphJSON = dash.create_plot(vendas, entradas , "outubro")
    return render_template('dashboard.html', graphJSON=graphJSON)

@app.route("/login")
def loginO():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port = 1404, debug = True)

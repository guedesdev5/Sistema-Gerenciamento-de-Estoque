from flask import Flask, render_template, request, flash, g
import backend.login as l
import backend.read as r
import backend.create as c
import backend.update as u

app = Flask(__name__)
app.secret_key = 'abcdohdohfhef32833'

@app.route("/")
def home():
    return render_template("login.html")
    
@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    result = l.getLogin(username, password)
    if result == 1:
        flash('Inserção realizada com sucesso!', 'success')
        readBD = r.readProdutos()
        readIdCategory = r.readIdCategory()
        readIdFornecedores = r.readIdFornecedores()
        permission = l.getPermission(username)
        if permission == 1:
            app.config['PERMISSION_USER'] = True
        else:
            app.config['PERMISSION_USER'] = False
        
        return render_template("homepage.html", lista = readBD, idCategory = readIdCategory, readIdFornecedores = readIdFornecedores, permissionUser = app.config['PERMISSION_USER'])
    else:
        flash('deu ruim', 'spam')
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
    result = c.createProdutos(id, name, description, price, quantity, category_id, fornecedor_id)
    print(result)
    readBD = r.readProdutos()
    readIdCategory = r.readIdCategory()
    readIdFornecedores = r.readIdFornecedores()
    print(readIdFornecedores)
    print(readIdCategory)
    if result == 1:
        return render_template("homepage.html", lista = readBD, idCategory = readIdCategory, readIdFornecedores = readIdFornecedores)
    else:
        return render_template("homepage.html", lista = readBD, idCategory = readIdCategory, readIdFornecedores = readIdFornecedores)

@app.route("/categorias", methods=['POST'])
def categoriaspost():
    name = request.form.get('name')
    description = request.form.get('description')
    result = c.createCategory(name, description)
    readBD = r.readCategory()
    if result == 1:
        return render_template("categorias.html", lista = readBD)
    else:
        return render_template("categorias.html", lista = readBD)
    
@app.route("/fornecedores", methods=['POST'])
def fornecedorespost():
    name = request.form.get('name')
    tel = request.form.get('tel')
    email = request.form.get('email')
    endereco = request.form.get('endereco')
    result = c.createFornecedor(name, tel, email, endereco)
    readBD = r.readFornecedor()
    print(result)
    if result == 1:
        return render_template("fornecedores.html", lista = readBD)
    else:
        return render_template("fornecedores.html", lista = readBD)

@app.route("/vendedores", methods=['POST'])
def vendedorespost():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    senha = request.form.get('password')
    permissao = request.form.get('permission')
    result = c.createVendedor(name, username, email, senha, permissao)
    readBD = r.readVender()
    print(result)
    if result == 1:
        return render_template("vendedores.html", lista = readBD)
    else:
        return render_template("vendedores.html", lista = readBD)
    
@app.route("/vendas", methods=['POST'])
def vendaspost():
    qntd = request.form.get('qntd')
    cd_produto = request.form.get('cod')
    cd_vendedor = request.form.get('codv')
    result = c.createVendas( qntd, cd_produto, cd_vendedor)
    readBD = r.readVendas()
    readIdVendedor = r.readIdvendedor()
    readIdProdutos = r.readIdprodutos()
    u.updateProductQntd(cd_produto, qntd)
    if result == 1:
        return render_template("vendas.html", lista = readBD, readIdVendedor = readIdVendedor, readIdProdutos = readIdProdutos, permissionUser = app.config['PERMISSION_USER'])
    else:
        return render_template("vendas.html", lista = readBD, readIdVendedor = readIdVendedor, readIdProdutos = readIdProdutos, permissionUser = app.config['PERMISSION_USER'])


@app.route("/vendedores.html")
def vendedores():
    readBD = r.readVender()
    return render_template("vendedores.html", lista = readBD)

@app.route("/homepage.html")
def homepage():
    readBD = r.readProdutos()
    readIdCategory = r.readIdCategory()
    readIdFornecedores = r.readIdFornecedores()
    return render_template("homepage.html", lista = readBD, idCategory = readIdCategory, readIdFornecedores = readIdFornecedores, permissionUser = app.config['PERMISSION_USER'])
  

@app.route("/categorias.html")
def categorias():
    readBD = r.readCategory()
    return render_template("categorias.html",  lista = readBD)

@app.route("/vendas.html")
def vendas():
    readBD = r.readVendas()
    readIdVendedor = r.readIdvendedor()
    readIdProdutos = r.readIdprodutos()
    return render_template("vendas.html", lista = readBD, readIdVendedor = readIdVendedor, readIdProdutos = readIdProdutos, permissionUser = app.config['PERMISSION_USER'])

@app.route("/fornecedores.html")
def fornecedores():
    readBD = r.readFornecedor()
    return render_template("fornecedores.html",  lista = readBD)

@app.route("/login.html")
def loginO():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug = True)

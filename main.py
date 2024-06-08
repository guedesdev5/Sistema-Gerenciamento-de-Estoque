from flask import Flask, render_template, request, flash
import backend.login as l
import backend.database as b

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
        readBD = b.read()
        return render_template("homepage.html", lista = readBD)
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
    result = b.create(id, name, description, price, quantity, category_id, fornecedor_id)
    readBD = b.read()
    if result == 1:
        return render_template("homepage.html", lista = readBD)
    else:
        return render_template("homepage.html", lista = readBD)

@app.route("/vendedores.html")
def vendedores():
    readBD = b.readVender()
    return render_template("vendedores.html", lista = readBD)

@app.route("/homepage.html")
def homepage():
    readBD = b.read()
    return render_template("homepage.html",  lista = readBD)

@app.route("/categorias.html")
def categorias():
    readBD = b.readCategory()
    return render_template("categorias.html",  lista = readBD)

@app.route("/fornecedores.html")
def fornecedores():
    readBD = b.readFornecedor()
    return render_template("fornecedores.html",  lista = readBD)

@app.route("/login.html")
def loginO():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug = True)

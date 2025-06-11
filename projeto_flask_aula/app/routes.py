from app import app
from flask import render_template
from app.forms.login_form import LoginForm
from app.controllers.authenticationController import authenticationController



@app.route("/")
def home():
    usuario = {
        'nome': 'Melqui',
        'produtos': ['Banana', 'Abacaxi']
    }
    esta_logado = True
    return render_template("index.html", usuario = usuario, usuario_logado = esta_logado)


@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route('/login', methods=('GET','POST'))
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return authenticationController.login(formulario)
    return render_template('login.html', title='login', form=formulario)
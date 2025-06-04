from app import app 
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return 'eu tenho 18 anos, sou bonito, e oto nivel'

@app.route('/endereco')
def endereco():
    return 'moro em ceará-mirim'

@app.route('/hobby')
def hobby():
    return 'sou videomaker, jogo games'
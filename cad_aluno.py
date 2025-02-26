# pip install flask
# faz a integração com páginas web

# flask --version

# a linha abaixo importa a bibliioteca Flask
from flask import Flask, render_template


# variável de aplicação
app = Flask(__name__)


@app.route('/ola')
def iniciando():
    return "<h2>Iniciando o projeto com flask</h2>"


# criando uma rota para a lista
@app.route('/lista')
def lista_alunos():
    return render_template('lista.html', titulo = 'FECAF')


# esse comadando tem que ser executado no final
app.run()
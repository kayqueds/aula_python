# pip install flask
# faz a integração com páginas web

# flask --version

# a linha abaixo importa a bibliioteca Flask
from flask import Flask, render_template

# a linha abaixo cria uma classe

class Aluno:
    # o self serve para acessar as propriedade
    # ela referencia a classe
    def __init__(self, ra, nome, idade, email):
        self.ra_aluno = ra
        self.nome_aluno = nome
        self.idade_aluno = idade
        self.email_aluno = email
        


# variável de aplicação para inicar
app = Flask(__name__)


# rota iniciaç
@app.route('/')
def home():
    return render_template('home.html')

# criando uma rota para a lista
@app.route('/lista')
def lista_alunos():
    
    # as 4 linhas abaixo, instanciam alunos
    aluno01 = Aluno("1001", "Carlos Adão", "19", "carlosadao@gmail.com")

    aluno02 = Aluno("1002", "Sérgio Figueiredo", "53", "sergiao@gmail.com")

    aluno03 = Aluno("1003", "Florinda Mesquita", "38", "florindames@gmail.com",)

    lista_alunos_cadastrados = [aluno01, aluno02, aluno03]

   


    # variavel alunos vai armazenar a lista
    return render_template('lista.html', titulo = 'FECAF',
    alunos = lista_alunos_cadastrados)



# esse comadando tem que ser executado no final
app.run(debug=True)
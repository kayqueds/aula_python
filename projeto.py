# pip install flask bilbioteca

# importa biblioteca para trabalhar
# com banco de dados
# obs: instalar o connector e sql alchemy
# pip install flask_sqlalchemy
from flask import  Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# a linha baixo cria uma calsse

# a linha importa a bilblioteca para trabalhar
# com banco de dados



app = Flask (__name__)

# CRIANDO UMA BIBLIOTECA PARA O BANCO DE DADOS
# configuração para conectar banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'toor',
        servidor = 'localhost',
        database = 'prj_cadastro'
    )


# a linha abaixo instancia o banco de dados
db = SQLAlchemy(app)

# a linha abaixo cria uma classe modelo,
# ou seja, uma classe referencia da tabela

class Aluno(db.Model): 
     ra_aluno = db.Column(db.Integer, primary_key = True, autoincrement = True)
     nome_aluno = db.Column(db.String(80), nullable = False)
     idade_aluno = db.Column(db.Integer, nullable = True)
     email_aluno = db.Column(db.String(120), nullable = False)


# método que vai representar aluno por aluno
     def __repr__(self):
         return "<Name %r>"% self.name


@app.route('/')
def home():
    return render_template('home.html')



@app.route("/lista")
def lista_alunos():

    # alista de alunos vai receber um select (query)
    lista_alunos_cadastrados = Aluno.query.order_by(Aluno.ra_aluno)

    return render_template("lista.html", titulo = 'UniFecaf', icone = '📝', 
                           alunos = lista_alunos_cadastrados)

# a partir daqui eu trabalho com a tela cadastrar.html
@app.route('/cadastro')
def cadastrar_aluno():
    return render_template('cadastrar.html')
# a rota/função abaixo, cadastra o aluno  na lista
# e posteriormente no banco de dados

# from flask_sqlalchemy import import SQLalchemy


# fazendo a conversão do tipo texto em int na idade
@app.route('/add_aluno', methods=['POST',])
def adicionar_aluno():
    nome_recebido = request.form['txtNome']
    idade_recebida = int(request.form['txtIdade'])
    email_recebeido = request.form['txtEmail']

    # após pegar as informações do aluno
    # devemos instaciar o aluno 
    novo_aluno = Aluno(nome_aluno = nome_recebido, idade_aluno = idade_recebida, email_aluno = email_recebeido)
    
    # a linha a baixo adiciona as informações do novo
    # aluno na lista
    
    # a linha abaixo adiciona os dados do aluno
    db.session.add(novo_aluno)

    # a linha abaixo grafa as informações no banco
    db.session.commit()



    return redirect('/lista')

app.run(debug=True)





# usuario banco: root
# senha do banco da Fecaf: toor
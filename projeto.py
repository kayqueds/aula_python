# pip install flask bilbioteca

# importa biblioteca para trabalhar
# com banco de dados
# obs: instalar o connector e sql alchemy
# pip install flask_sqlalchemy
<<<<<<< HEAD
from flask import  Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

=======
from flask import  Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
>>>>>>> e0ab082d99397955ad1728d9802f4792596c4ad0
# a linha baixo cria uma calsse

# a linha importa a bilblioteca para trabalhar
# com banco de dados



app = Flask (__name__)

<<<<<<< HEAD
app.secret_key = 'projetoflask'

=======
>>>>>>> e0ab082d99397955ad1728d9802f4792596c4ad0
# CRIANDO UMA BIBLIOTECA PARA O BANCO DE DADOS
# configuração para conectar banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'root',
<<<<<<< HEAD
        senha = 'toor',
=======
<<<<<<< HEAD
        senha = 'toor',
=======
        senha = '',
>>>>>>> 9690b916e191d8190d10cb9f3aa81ad11263a738
>>>>>>> e0ab082d99397955ad1728d9802f4792596c4ad0
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

<<<<<<< HEAD
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect('/login')


=======
>>>>>>> e0ab082d99397955ad1728d9802f4792596c4ad0
    # alista de alunos vai receber um select (query)
    lista_alunos_cadastrados = Aluno.query.order_by(Aluno.ra_aluno)

    return render_template("lista.html", titulo = 'UniFecaf', icone = '📝', 
                           alunos = lista_alunos_cadastrados)

# a partir daqui eu trabalho com a tela cadastrar.html
<<<<<<< HEAD


@app.route('/cadastrar')
def cadastrar_aluno():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:

        return redirect('/login')

    return render_template('cadastrar.html')
=======
@app.route('/cadastro')
def cadastrar_aluno():
    return render_template('cadastrar.html', cache_timeout=0)
>>>>>>> e0ab082d99397955ad1728d9802f4792596c4ad0
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

<<<<<<< HEAD
# aqui começa a parte de atualizar o cadastro
=======

>>>>>>> e0ab082d99397955ad1728d9802f4792596c4ad0

    return redirect('/lista')



# o editar precisa do RA

@app.route('/editar/<int:ra>')
def editar_aluno(ra):
    
    # a linha abaixo busca o aluno referente ao RA passado
    # vai pegar o ra do aluno da classe Aluno
    aluno_selecionado = Aluno.query.filter_by(ra_aluno = ra).first()

    return render_template('editar.html', aluno = aluno_selecionado)

@app.route('/atualiza', methods=['POST'])
def atualizar_aluno():
    
    # a linha abaixo identifica o aluno para garantir a atualização corretamente
    aluno_atualizado = Aluno.query.filter_by(ra_aluno = request.form['txtRA']).first()

    # a linha abaixo altera as informações
    aluno_atualizado.nome_aluno = request.form['txtNome']
    aluno_atualizado.idade_aluno = request.form['txtIdade']
    aluno_atualizado.email_aluno = request.form['txtEmail']

    # a linha abaixo adiciona os novos dados
    db.session.commit()

    return redirect('/lista')



# a partir daqui vamos fazer a rota para excluir o aluno
@app.route('/excluir/<int:ra>')  
def excluir_aluno(ra):
    
   # a linha abaixo exclui o aluno
   Aluno.query.filter_by(ra_aluno = ra).delete()

   db.session.commit()
   return redirect('/lista')    


# rota de login
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods= ['POST'])
def autenticar_usuario():
    login = request.form['txtLogin']
    senha = request.form['txtSenha']



    if login == 'admin' and senha == 'admin':
        # a linha abaixo cria uma sessão para o usuário após logar    
        session['usuario_logado'] = request.form['txtLogin']

        return redirect ('/lista')
    else:
        return redirect('/login')




@app.route('/sair')
def sair():
    session['usuario_logado'] = None

    return redirect('/login')

app.run(debug=True)





# usuario banco: root
# senha do banco da Fecaf: toor
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'projetoflask'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB='mysql+mysqlconnector',
        usuario='root',
        senha='toor',
        servidor='localhost',
        database='prj_cadastro'
    )

db = SQLAlchemy(app)

class Aluno(db.Model): 
     ra_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True)
     nome_aluno = db.Column(db.String(80), nullable=False)
     idade_aluno = db.Column(db.Integer, nullable=True)
     email_aluno = db.Column(db.String(120), nullable=False)

     def __repr__(self):
         return "<Name %r>" % self.nome_aluno

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/lista")
def lista_alunos():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    lista_alunos_cadastrados = Aluno.query.order_by(Aluno.ra_aluno)
    return render_template("lista.html", titulo='UniFecaf', icone='📝', alunos=lista_alunos_cadastrados)

@app.route('/cadastrar')
def cadastrar_aluno():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    return render_template('cadastrar.html')

@app.route('/add_aluno', methods=['POST'])
def adicionar_aluno():
    nome_recebido = request.form['txtNome']
    idade_recebida = int(request.form['txtIdade'])
    email_recebeido = request.form['txtEmail']

    novo_aluno = Aluno(nome_aluno=nome_recebido, idade_aluno=idade_recebida, email_aluno=email_recebeido)
    db.session.add(novo_aluno)
    db.session.commit()
    return redirect('/lista')

@app.route('/editar/<int:ra>')
def editar_aluno(ra):
    aluno_selecionado = Aluno.query.filter_by(ra_aluno=ra).first()
    return render_template('editar.html', aluno=aluno_selecionado)

@app.route('/atualiza', methods=['POST'])
def atualizar_aluno():
    aluno_atualizado = Aluno.query.filter_by(ra_aluno=request.form['txtRA']).first()
    aluno_atualizado.nome_aluno = request.form['txtNome']
    aluno_atualizado.idade_aluno = request.form['txtIdade']
    aluno_atualizado.email_aluno = request.form['txtEmail']
    db.session.commit()
    return redirect('/lista')

@app.route('/excluir/<int:ra>')
def excluir_aluno(ra):
    Aluno.query.filter_by(ra_aluno=ra).delete()
    db.session.commit()
    return redirect('/lista')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar_usuario():
    login = request.form['txtLogin']
    senha = request.form['txtSenha']
    if login == 'admin' and senha == 'admin':
        session['usuario_logado'] = login
        return redirect('/lista')
    else:
        return redirect('/login')

@app.route('/sair')
def sair():
    session['usuario_logado'] = None
    return redirect('/login')

app.run(debug=True)

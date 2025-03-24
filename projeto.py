# pip install flask bilbioteca

# importa biblioteca
from flask import  Flask, render_template, request, redirect

# a linha baixo cria uma calsse
class Aluno:
    def __init__(self, ra, nome, idade, email):
        self.ra_aluno = ra
        self.nome_aluno = nome
        self.idade_aluno = idade
        self.email_aluno = email


 # as 3 linhas abaixo, instanciam alunos 
aluno01 = Aluno('1001', 'Daniel Xavier', '32',
                    'daniel@pro,fecaf.com.br')
    
aluno02 = Aluno('1002', 'Alex Silveira', '27', 
                    'alex@a.fecaf.com.br')

aluno03 = Aluno('1003', 'Raisa magalhaes', '22',
                    'raisa@a.fecaf.com.br') 

lista_alunos_cadastrados = [aluno01, aluno02, aluno03]


app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route("/lista")
def lista_alunos():

    

    return render_template("lista.html", titulo = 'UniFecaf', icone = '📝', 
                           alunos = lista_alunos_cadastrados)

# a partir daqui eu trabalho com a tela cadastrar.html
@app.route('/cadastrar')
def cadastrar_aluno():
    return render_template('cadastrar.html')
# a rota/função abaixo, cadastra o aluno  na lista
# e posteriormente no banco de dados

@app.route('/add_aluno', methods=['POST',])
def adicionar_aluno():
    nome_recebido = request.form['txtNome']
    idade_recebida = request.form['txtIdade']
    email_recebeido = request.form['txtEmail']
    ra_recebido = request.form['txtRA']

    # após pegar as informações do aluno
    # devemos instaciar o aluno 
    novo_aluno = Aluno(ra_recebido, nome_recebido,
                       idade_recebida,email_recebeido)
    
    # a linha a baixo adiciona as informações do novo
    # aluno na lista
    lista_alunos_cadastrados.append(novo_aluno)

    return redirect('/lista')

app.run(debug=True)



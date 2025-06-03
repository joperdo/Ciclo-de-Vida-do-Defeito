import secrets
from flask import Flask, render_template, request, redirect, url_for, flash
from src.models.pessoa import Pessoa
from src.controllers.pessoa_controller import PessoaController
from src.database import init_app, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Gera uma chave secreta segura

# Inicializa o banco de dados com a aplicação
init_app(app)

@app.route('/')
def index():
    """Página inicial."""
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_pessoa():
    """Rota para cadastrar uma nova pessoa."""
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        sobrenome = request.form['sobrenome'].strip()
        cpf = request.form['cpf'].strip()
        data_nascimento = request.form['data_nascimento'].strip()

        # Validação mínima
        if not nome or not cpf:
            flash('Nome e CPF são obrigatórios.', 'warning')
            return render_template('cadastrar.html')

        try:
            PessoaController.salvar_pessoa(nome, sobrenome, cpf, data_nascimento)
            flash('Pessoa cadastrada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except Exception as err:
            flash(f'Erro ao cadastrar: {str(err)}', 'danger')
    return render_template('cadastrar.html')

@app.route('/listar')
def listar_pessoas():
    """Rota para listar todas as pessoas cadastradas."""
    pessoas = Pessoa.query.all()
    return render_template('listar.html', pessoas=pessoas)

@app.route('/editar/<int:id_pessoa>', methods=['GET', 'POST']) #correção da variável id para id_pessoa
def editar_pessoa(id_pessoa):
    """Rota para editar uma pessoa existente."""
    pessoa = Pessoa.query.get_or_404(id_pessoa)
    if request.method == 'POST':
        pessoa.nome = request.form['nome'].strip()
        pessoa.sobrenome = request.form['sobrenome'].strip()
        pessoa.cpf = request.form['cpf'].strip()
        pessoa.data_de_nascimento = request.form['data_nascimento'].strip()

        try:
            db.session.commit()
            flash('Pessoa atualizada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except Exception as err:
            flash(f'Erro ao atualizar: {str(err)}', 'danger')
    return render_template('editar.html', pessoa=pessoa)

@app.route('/remover/<int:id_pessoa>') #correção da variável id para id_pessoa
def remover_pessoa(id_pessoa):
    """Rota para remover uma pessoa existente."""
    try:
        pessoa = Pessoa.query.get_or_404(id_pessoa)
        db.session.delete(pessoa)
        db.session.commit()
        flash('Pessoa removida com sucesso!', 'success')
    except Exception as err:
        flash(f'Erro ao remover: {str(err)}', 'danger')
    return redirect(url_for('listar_pessoas'))

if __name__ == '__main__':
    app.run(debug=True)

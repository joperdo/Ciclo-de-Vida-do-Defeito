from flask_sqlalchemy import SQLAlchemy

# Instancia o objeto SQLAlchemy (deve ser feito fora da função para reuso global)
db = SQLAlchemy()

def init_app(app):
    """
    Inicializa a extensão SQLAlchemy com a aplicação Flask e
    cria todas as tabelas no banco de dados com base nos modelos definidos.
    
    :param app: Instância da aplicação Flask
    """
    # Inicializa o SQLAlchemy com a instância da aplicação
    db.init_app(app)

    # Cria o contexto da aplicação para garantir que o banco seja criado
    # apenas dentro de um ambiente com acesso ao app atual
    with app.app_context():
        # Cria todas as tabelas do banco de dados com base nos modelos declarados
        db.create_all()

"""
    Definição do modelo Pessoa.
"""

from database import db

class Pessoa(db.Model):
    """Modelo que representa uma pessoa na base de dados."""

    __tablename__ = 'pessoas'  # Nome explícito da tabela no banco 

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_de_nascimento = db.Column(db.String(10), nullable=False)  

    def __repr__(self):
        """Representação legível do objeto Pessoa para depuração."""
        return f'<Pessoa {self.id} - {self.nome} {self.sobrenome}>'

    def to_dict(self):
        """Método utilitário para converter o objeto em dicionário."""
        return {
            "id": self.id,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cpf": self.cpf,
            "data_de_nascimento": self.data_de_nascimento
        }

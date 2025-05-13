from models.pessoa import Pessoa
from database import db

class PessoaController:
    @staticmethod
    def salvar_pessoa(nome, sobrenome, cpf, data_nascimento):
        """Cria e salva uma nova pessoa no banco de dados."""
        
        # Verificação simples de dados obrigatórios (evita salvar dados em branco)
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")

        # Remove espaços extras (boa prática)
        nome = nome.strip()
        sobrenome = sobrenome.strip() if sobrenome else ''
        cpf = cpf.strip()
        data_nascimento = data_nascimento.strip() if data_nascimento else None

        pessoa = Pessoa(
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,
            data_de_nascimento=data_nascimento
        )

        # Adiciona e confirma no banco
        db.session.add(pessoa)
        db.session.commit()

    @staticmethod
    def listar_pessoas():
        """Retorna todas as pessoas cadastradas."""
        return Pessoa.query.all()

    @staticmethod
    def remover_pessoa(pessoa):
        """Remove a pessoa informada do banco de dados."""
        if not pessoa:
            raise ValueError("Pessoa inválida para remoção.")
        
        db.session.delete(pessoa)
        db.session.commit()

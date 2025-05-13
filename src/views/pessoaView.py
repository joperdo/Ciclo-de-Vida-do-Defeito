from ..controllers.pessoa_controller import PessoaController
from ..models.pessoa import Pessoa

"""
    View responsável por adicionar, remover, atualizar e listar pessoas.
"""

def adicionarPessoa():
    cpf = input("Digite o CPF da pessoa: ").strip()
    
    if verificaCPF(cpf):
        print('\nCPF informado já está cadastrado!')
        return
    
    nome = input("Digite o nome da pessoa: ").strip()
    sobrenome = input("Digite o sobrenome da pessoa: ").strip()
    data_de_nascimento = input("Digite a data de nascimento da pessoa: ").strip()

    nova_pessoa = Pessoa(
        nome=nome,
        sobrenome=sobrenome,
        cpf=cpf,
        data_de_nascimento=data_de_nascimento
    )
    
    PessoaController.salvar_pessoa(nome, sobrenome, cpf, data_de_nascimento)
    print('\n---- Cadastro realizado com sucesso! ----')


def buscarPessoa():
    cpf = input('Digite o CPF da pessoa: ').strip()

    for pessoa in PessoaController.listar_pessoas():
        if pessoa.cpf == cpf:
            print(f'\nNome: {pessoa.nome}\nSobrenome: {pessoa.sobrenome}\nCPF: {pessoa.cpf}\nData de Nascimento: {pessoa.data_de_nascimento}')
            return

    print('\nCPF da pessoa informada não possui cadastro.')


def atualizarPessoa():
    cpf = input('Digite o CPF da pessoa: ').strip()
    
    for pessoa in PessoaController.listar_pessoas():
        if pessoa.cpf == cpf:
            novo_nome = input('Digite o novo nome da pessoa: ').strip()
            novo_sobrenome = input('Digite o novo sobrenome da pessoa: ').strip()
            
            pessoa.nome = novo_nome
            pessoa.sobrenome = novo_sobrenome
            # Aqui poderia haver PessoaController.atualizar_pessoa(pessoa) se existisse
            PessoaController.salvar_pessoa(
                pessoa.nome, pessoa.sobrenome, pessoa.cpf, pessoa.data_de_nascimento
            )  # reutilizando a função para atualizar também
            print('\nDados atualizados com sucesso!')
            return

    print('\nCPF da pessoa informada não possui cadastro.')


def listarPessoas():
    pessoas = PessoaController.listar_pessoas()
    
    if not pessoas:
        print('\nNão há pessoas cadastradas no momento!')
        return
    
    print('\nLista de Pessoas Cadastradas:')
    for pessoa in pessoas:
        print('------------------------')
        print(f'Nome: {pessoa.nome}\nSobrenome: {pessoa.sobrenome}\nCPF: {pessoa.cpf}\nData de Nascimento: {pessoa.data_de_nascimento}')


def removerPessoa():
    cpf = input('Digite o CPF da pessoa: ').strip()
    
    for pessoa in PessoaController.listar_pessoas():
        if pessoa.cpf == cpf:
            PessoaController.remover_pessoa(pessoa)
            print(f'\nCPF: {pessoa.cpf} foi removido com sucesso!')
            return

    print('\nCPF da pessoa informada não possui cadastro.')


def verificaCPF(cpf):
    """
    Verifica se um CPF já está cadastrado.
    Retorna True se existir, False caso contrário.
    """
    for pessoa in PessoaController.listar_pessoas():
        if pessoa.cpf == cpf:
            return True
    return False

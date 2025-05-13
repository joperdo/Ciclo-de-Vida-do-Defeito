from .pessoaView import *

"""
    View responsável pela tela principal da aplicação (modo console).
"""

# ------------------------------------------------
#  Menu de navegação
# ------------------------------------------------

MENU_TEXTO = """
---- Sistema de CRUD em Python -----

[c] - Cadastrar pessoa
[b] - Buscar pessoa
[a] - Atualizar pessoa
[l] - Listar pessoas
[d] - Deletar pessoa
[q] - Sair do sistema

Escolha uma opção: """

def menu_navegacao():
    """Função principal para navegação no menu de opções."""
    while True:
        try:
            opcao = input(MENU_TEXTO).strip().lower()  # Remove espaços e força minúsculo

            match opcao:
                case 'c':
                    adicionarPessoa()
                case 'b':
                    buscarPessoa()
                case 'a':
                    atualizarPessoa()
                case 'l':
                    listarPessoas()
                case 'd':
                    removerPessoa()
                case 'q':
                    print('=== Finalizando sistema... ===')
                    break  # Usa break em vez de exit para melhor controle
                case _:
                    print("Opção inválida! Tente novamente.")
        except KeyboardInterrupt:
            print("\nEncerrando o sistema por interrupção do usuário.")
            break
        except Exception as err:
            print(f"Ocorreu um erro: {err}")

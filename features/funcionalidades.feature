Feature: Funcionalidades principais do sistema de pessoas

  Scenario: Cadastrar uma nova pessoa com dados válidos
    Given que o sistema está inicializado
    When eu cadastro uma pessoa com nome "João", sobrenome "Silva", CPF "12345678900" e data de nascimento "2000-01-01"
    Then a pessoa com CPF "12345678900" deve estar cadastrada no sistema

  Scenario: Editar os dados de uma pessoa existente
    Given que o sistema está inicializado
    And uma pessoa com CPF "98765432100" já está cadastrada
    When eu atualizo essa pessoa para nome "Maria" e sobrenome "Souza"
    Then os dados da pessoa com CPF "98765432100" devem refletir as alterações

  Scenario: Listar pessoas cadastradas
    Given que o sistema está inicializado
    And uma pessoa com CPF "11122233344" já está cadastrada
    When eu acesso a listagem de pessoas
    Then o CPF "11122233344" deve aparecer na lista

  Scenario: Remover uma pessoa existente
    Given que o sistema está inicializado
    And uma pessoa com CPF "22233344455" já está cadastrada
    When eu removo a pessoa com CPF "22233344455"
    Then a pessoa com CPF "22233344455" não deve mais estar no sistema

  Scenario: Tentar cadastrar uma pessoa com CPF já existente
    Given que o sistema está inicializado
    And uma pessoa com CPF "33344455566" já está cadastrada
    When eu tento cadastrar novamente uma pessoa com nome "Carlos", sobrenome "Oliveira", CPF "33344455566" e data de nascimento "1999-09-09"
    Then o sistema não deve permitir duplicidade de CPF

  Scenario: Tentar cadastrar uma pessoa com nome vazio
    Given que o sistema está inicializado
    When eu tento cadastrar uma pessoa com nome "", sobrenome "Souza", CPF "44455566677" e data de nascimento "2001-01-01"
    Then o sistema deve rejeitar o cadastro por nome vazio

  Scenario: Tentar remover uma pessoa com CPF inexistente
    Given que o sistema está inicializado
    When eu tento remover a pessoa com CPF "00000000000"
    Then nenhuma pessoa deve ser removida e o sistema deve continuar funcionando

  Scenario: Tentar cadastrar uma pessoa com todos os campos vazios
    Given que o sistema está inicializado
    When eu tento cadastrar uma pessoa com nome "", sobrenome "", CPF "", e data de nascimento ""
    Then o sistema deve rejeitar o cadastro por dados vazios

  Scenario: Tentar cadastrar uma pessoa com CPF menor que 11 dígitos
    Given que o sistema está inicializado
    When eu tento cadastrar uma pessoa com nome "Teste", sobrenome "Curto", CPF "12345", e data de nascimento "2000-01-01"
    Then o sistema deve rejeitar o CPF por tamanho inválido

  Scenario: Tentar cadastrar uma pessoa com CPF contendo letras
    Given que o sistema está inicializado
    When eu tento cadastrar uma pessoa com nome "Lucas", sobrenome "Letra", CPF "abc123xyz", e data de nascimento "2000-01-01"
    Then o sistema deve rejeitar o CPF por conter caracteres inválidos


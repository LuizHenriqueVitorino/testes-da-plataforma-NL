# language: pt

Funcionalidade: Testar o sistema de cadastro colocando dados incorretos no cpf

    Contexto: acessar página teste
        Dado que acessa a seção de cadastro da página NL
    
    Cenário: acessar a página NL e falhar no cadastro por conta de um cpf em branco
        Dado que preenche o campo cpf com branco
        Dado que preenche o campo senha
        Dado que preenche o campo confirme a senha
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo falhar no cadastro
        
# language: pt

Funcionalidade: Testar o sistema de cadastro da página NL

    Contexto: acessar página teste
        Dado que acessa a seção de cadastro da página NL

    Cenário: acessar a página NL e falhar no cadastro por conta da senha em branco
        Dado que preenche o campo cpf
        Dado que preenche o campo senha em branco
        Dado que preenche o campo confirme a senha em branco
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo falhar no cadastro
        
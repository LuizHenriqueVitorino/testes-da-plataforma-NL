# language: pt

Funcionalidade: Testar o sistema de cadastro da página NL

    Contexto: Acessar página NL
        Dado que acessa a seção de cadastro da página NL

    Cenário: acessar a página NL e falhar no cadastro por conta do confirme senha estar diferente da senha
        Dado que preenche o campo cpf
        Dado que preenche o campo senha
        Dado que preenche o campo confirme a senha diferente de senha
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo falhar no cadastro


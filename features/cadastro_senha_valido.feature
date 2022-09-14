# language: pt

Funcionalidade: Testar o sistema de cadastro da página NL

    Contexto: acessar página teste
        Dado que acessa a seção de cadastro da página NL

    Cenário: acessar a página NL e realizar o cadastro com uma senha valida
        Dado que preenche o campo cpf
        Dado que preenche o campo senha
        Dado que preenche o campo confirme a senha
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo passar para o preenchimento dos próximos dados
       
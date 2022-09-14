# language: pt

Funcionalidade: Testar o sistema de cadastro da página NL

    Contexto: acessar página de teste
        Dado que acessa a seção de cadastro da página NL

    Cenário: acessar a página NL e falhar no cadastro por conta de um cpf inválido
        Dado que preenche o campo cpf de forma invalida
        Dado que preenche o campo senha
        Dado que preenche o campo confirme a senha
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo falhar no cadastro

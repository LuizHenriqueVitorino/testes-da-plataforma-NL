# language: pt

Funcionalidade: Testar o sistema de cadastro da página NL

    Contexto: acessar página teste
        Dado que acessa a seção de cadastro da página NL

    Cenário: acessar a página NL e falhar no cadastro por conta da senha invalida
        Dado que preenche o campo cpf
        #TODO Verificar com o Luiz como devem ficar os testes de senha
        Dado que preenche o campo senha invalida
        #TODO implementar o dado e na hora dos dados utilizar o E.
        Dado que preenche o campo confirme a senha repetindo senha
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo falhar no cadastro
       
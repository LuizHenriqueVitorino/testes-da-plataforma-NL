# language: pt

Funcionalidade: Cadastrar um usuário na plataforma NL

    Contexto: acessar página de teste
        Dado que acessa a seção de cadastro da página NL

    Cenário: acessar pagina NL e realizar cadastro de um usuário
        Dado que preenche o campo cpf
        Dado que preenche o campo senha
        Dado que preenche o campo confirme a senha
        Dado que preenche o campo e-mail
        Quando clico no botão cadastrar
        Então devo passar para o preenchimento dos próximos dados

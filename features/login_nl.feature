# language: pt

Funcionalidade: realizar login na plataforma NL

    #Contextos são ações que serão execultadas antes de cada teste
    Contexto: acessar página de teste
        Dado que acesso a página do NL

    Cenário: acessar página NL e realizar login
        Dado que preencho o campo cpf
        Dado que preencho o campo senha
        Quando clico no botão entrar
        Então devo logar no sistema
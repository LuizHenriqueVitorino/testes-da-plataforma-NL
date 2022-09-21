# language: pt

Funcionalidade: Testar a aba de pesquisador da página NL

    Contexto: Acessar o menu principal da página NL
        Dado que realiza o login do usuário
    
    Cenário: entrar na aba dashboard e testar se aba está presente verificando o titulo da mesma
        Dado que acessa seus números e vai a dashboard
        Então a aba dashboard deve aparecer
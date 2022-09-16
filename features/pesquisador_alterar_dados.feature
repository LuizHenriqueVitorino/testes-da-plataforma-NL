# language: pt

Funcionalidade: Testar a aba de pesquisador da página NL

    Contexto: Acessar o menu principal da página NL
        Dado que realiza o login do usuário
    
    Cenário: Entrar no setor de alterar dados e comparar o titulo da aba com o do menu
        Dado que acessa alterar seus dados
        Então o titulo da aba deve ser igual ao do menu 
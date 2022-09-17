# language: pt

Funcionalidade: Testar a aba de pesquisador da página NL

    Contexto: Acessar o menu principal da página NL
        Dado que realiza o login do usuário
    
    Cenário: Entrar no setor de alterar dados e comparar o campo cpf com o do login
        Dado que acessa alterar seus dados
        Então o campo cpf deve ser igual ao de login 
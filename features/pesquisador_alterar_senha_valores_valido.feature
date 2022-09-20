# language: pt

Funcionalidade: Testar a aba de pesquisador da página NL

    Contexto: Acessar o menu principal da página NL
        Dado que realiza o login do usuário
    
    Cenário: Entrar no setor de alterar senha e modificar a senha
        Dado que acessa alterar senha
        E preenche os campos de senha de forma correta
        Então a senha deve ser alterada
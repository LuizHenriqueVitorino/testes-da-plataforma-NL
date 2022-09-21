# language: pt

Funcionalidade: Testar a aba de pesquisador da página NL

    Contexto: Acessar o menu principal da página NL
        Dado que realiza o login do usuário
    
    Cenário: Entrar no setor de mesagens do sistema e verificar se a data e a hora estão condizentes com as informações da página principal.
        Dado que acessa mensagens do sistema
        E acessa os detalhes de uma das mensagens
        Então a data e hora devem estar iguais na página principal e nos detelhes
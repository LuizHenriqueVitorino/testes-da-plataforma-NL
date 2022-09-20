# language: pt

Funcionalidade: Testar a aba de pesquisador da página NL

    Contexto: Acessar o menu principal da página NL
        Dado que realiza o login do usuário
    
    Cenário: Entrar no setor de alterar senha e falhar ao modificar a senha por conta da nova senha ser incorreta juntamente com o confirme senha
        Dado que acessa alterar senha
        E preenche os campos de senha e confirme senha de forma incorreta
        Então a senha devo falhar na alteração das senhas
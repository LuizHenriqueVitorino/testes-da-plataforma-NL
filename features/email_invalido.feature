# language: pt

Funcionalidade: Testar o campo de email na página de cadastro NL

    Contexto: acessar página teste
        Dado que acessa a seção de cadastro da página NL em específico o campo de email
    
    Cenário: acessar a página de cadastro NL e falhar no processo por conta de uma tentativa falha de concluir inserindo
    um email inválido no campo de email 
        Dado que preenche o campo cpf
        Dado que preenche o campo senha
        Dado que preenche o campo confirme a senha
        Dado que preenche o campo e-mail inválido
        Quando clico no botão cadastrar
        Então devo falhar no cadastro
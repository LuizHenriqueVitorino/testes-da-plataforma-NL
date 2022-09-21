# language: pt

Funcionalidade: Testar os projetos em execução dentro da página NL

    Contexto: acessar a aba de (Documentos Gerais e Modelos).
        Dado que acessa a aba de "Projetos"
        Dado que acessa a aba de "Documentos Gerais e Modelos"

    Cenário: obter êxito em acessar a aba (Documentos Gerais e Modelos) para conseguir
    obter as informações dos documentos gerais e modelos.
        Dado que clica em Projetos
        Dado que clica em Documentos Gerais e Modelos  
        Então a aba de (Documentos Gerais e Modelos) é aberta.
        Dado que clica na logo (plataforma NL). 
        E clica em fechar a aba de (Documentos Gerais e Modelos).



# language: pt

Funcionalidade: Testar os projetos em execução dentro da página NL

    Contexto: acessar a aba de (Listar em execução e executados).
        Dado que acessa a aba de "Projetos"
        Dado que acessa a aba de "Listar em execução e executados" dentro de "Projetos"

    Cenário: obter êxito em acessar a aba (Listar em execução e executados) para conseguir
    obter as informações dos projetos mostrados.
        Dado que clica em Projetos
        Dado que clica em Listar em execução e executados  
        Então a aba de (Listar em execução e executados) é aberta.



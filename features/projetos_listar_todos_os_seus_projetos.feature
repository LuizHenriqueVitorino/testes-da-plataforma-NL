# language: pt

Funcionalidade: Testar os projetos em execução dentro da página NL

    Contexto: acessar a aba de (Listar todos os seus projetos).
        Dado que acessa a aba de "Projetos"
        Dado que acessa a aba de "Listar todos os seus projetos" dentro de "Projetos"

    Cenário: obter êxito em acessar a aba (Listar todos os seus projetos) para conseguir
    obter as informações dos projetos mostrados.
        Dado que clica em Projetos
        Dado que clica em Listar todos os seus projetos  
        Então a aba de (Listar todos os seus projetos) é aberta.


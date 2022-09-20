# language: pt

Funcionalidade: Testar os projetos em execução dentro da página NL

    Contexto: acessar a aba de (Enviar Documentação).
        Dado que acessa a aba de "Projetos"
        Dado que acessa a aba de "Exclusivo para Bolsistas" 
        Dado que acessa a aba de "Enviar Documentação"

    Cenário: obter êxito em acessar a aba (Enviar Documentação) para conseguir enviar
    os devidos documentos
        Dado que clica em Projetos
        Dado que clica em Exclusivo para Bolsistas
        Dado que clica em Enviar Documentação
        Então a aba de (Enviar Documentação) é aberta.
        E clica em fechar a aba de (Enviar Documentação).



# language: pt

Funcionalidade: Testar os projetos em execução dentro da página NL

    Contexto: acessar a aba de (Enviar Relatório).
        Dado que acessa a aba de "Projetos"
        Dado que acessa a aba de "Exclusivo para Bolsistas" dentro de "Projetos"
        Dado que acessa a aba de "Enviar Relatório" dentro de "Exclusivo para Bolsistas"
            que fica dentro de "Projetos"

    Cenário: obter êxito em acessar a aba (Enviar Relatório) para conseguir enviar
    os devidos relatórios
        Dado que clica em Projetos
        Dado que clica em Exclusivo para Bolsistas
        Dado que clica em Enviar Relatório
        Então a aba de (Enviar Relatório) é aberta.
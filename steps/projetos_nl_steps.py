from behave import *
from pages.projetos_documentos_gerais_e_modelos_page import NLDocumentosGeraisEModelos
from pages.projetos_exclusivo_para_bolsistas_enviar_documentacao_page import NLExclusivoParaBolsistasEnviarDocumentacao
from pages.projetos_exclusivo_para_bolsistas_enviar_relatorio_page import NLExclusivoParaBolsistasEnviarRelatorio
from pages.projetos_listar_em_execucao_e_executados_page import NLListarEmExecucaoEExecutados
from pages.projetos_listar_todos_os_seus_projetos_page import NLListarTodosOsSeusProjetos
from support import Support
from selenium.webdriver.common.by import By
from login import Login

login = Login()
sup = Support()
nldgm = NLDocumentosGeraisEModelos()
nlepbed = NLExclusivoParaBolsistasEnviarDocumentacao()
nlepber = NLExclusivoParaBolsistasEnviarRelatorio()
nlleeee = NLListarEmExecucaoEExecutados()
nlltosp = NLListarTodosOsSeusProjetos()

@given(u'que acessa a aba de "Projetos"')
def step_impl(context):
    nldgm.acessar_aba_projetos()

@given(u'que clica em Listar em execução e executados')
def step_impl(context):
    nlleeee.acessar_listar_em_execucao_e_executados()

@given(u'que acessa a aba de "Documentos Gerais e Modelos"')
def step_impl(context):
    nldgm.acessar_doc_gerais_e_modelos()


@given(u'que clica em Projetos')
def step_impl(context):
    nlepbed.acessar_aba_projetos()


@given(u'que clica em Documentos Gerais e Modelos')
def step_impl(context):
    nldgm.acessar_doc_gerais_e_modelos()


@then(u'a aba de (Documentos Gerais e Modelos) é aberta.')
def step_impl(context):
    nldgm.procurar_documentos_na_pag()

@given(u'que acessa a aba de "Exclusivo para Bolsistas"')
def step_impl(context):
    nlepbed.acessar_aba_exclusivo_para_bolsistas()


@given(u'que acessa a aba de "Enviar Documentação"')
def step_impl(context):
    nlepbed.acessar_aba_enviar_documentacao()


@given(u'que clica em Exclusivo para Bolsistas')
def step_impl(context):
    nlepbed.acessar_aba_exclusivo_para_bolsistas()


@given(u'que clica em Enviar Documentação')
def step_impl(context):
    nlepbed.acessar_aba_enviar_documentacao()


@then(u'a aba de (Enviar Documentação) é aberta.')
def step_impl(context):
    nlepbed.procurar_enviar_documentacao()


@given(u'que acessa a aba de "Enviar Relatório"')
def step_impl(context):
    nlepber.acessar_enviar_relatorio()


@given(u'que clica em Enviar Relatório')
def step_impl(context):
    nlepber.acessar_enviar_relatorio()


@then(u'a aba de (Enviar Relatório) é aberta.')
def step_impl(context):
    nlepber.procurar_enviar_relatorio()


@given(u'que acessa a aba de "Listar em execução e executados"')
def step_impl(context):
    nlleeee.acessar_listar_em_execucao_e_executados()

@then(u'a aba de (Listar em execução e executados) é aberta.')
def step_impl(context):
    nlleeee.procurar_listar_em_execucao_e_executados()


@given(u'que acessa a aba de "Listar todos os seus projetos"')
def step_impl(context):
    nlltosp.acessar_todos_os_seus_projetos()


@given(u'que clica em Listar todos os seus projetos')
def step_impl(context):
    nlltosp.acessar_todos_os_seus_projetos()


@then(u'a aba de (Listar todos os seus projetos) é aberta.')
def step_impl(context):
    nlltosp.procurar_listar_todos_os_seus_projetos()

@then(u'clica em fechar a aba de (Documentos Gerais e Modelos).')
def step_impl(context):
    nldgm.fechar_doc_gerais_e_modelos()


@then(u'clica em fechar a aba de (Enviar Documentação).')
def step_impl(context):
    nlepbed.fechar_aba_enviar_documentacao()


@then(u'clica em fechar a aba de (Enviar relatório).')
def step_impl(context):
    nlepber.fechar_aba_enviar_relatorio()


@then(u'clica em fechar a aba de (Listar em execução e executados).')
def step_impl(context):
    nlleeee.fechar_aba_listar_em_execucao_e_executados()


@then(u'clica em fechar a aba de (Listar todos os seus projetos).')
def step_impl(context):
    nlltosp.fechar_aba_listar_todos_os_seus_projetos()
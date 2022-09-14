from behave import *
from pages.cadastro_nl_page import NLCadastroPage
from support import Support
from selenium.webdriver.common.by import By

nlcp = NLCadastroPage()
sup = Support()

@given(u'que acessa a seção de cadastro da página NL')
def step_impl(context):
    nlcp.acessar_Nl('https://prpi.ifce.edu.br/nl/app_form_add_users/')

@given(u'que preenche o campo cpf de forma invalida')
def step_impl(context):
    nlcp.escrever_cpf('12345677777')

@given(u'que preenche o campo cpf')
def step_impl(context):
    nlcp.escrever_cpf(sup.cpf_generator())

@given(u'que preenche o campo cpf com branco')
def step_impl(context):
    nlcp.escrever_cpf('')

@given(u'que preenche o campo senha')
def step_impl(context):
    nlcp.escrever_senha('123456')

@given(u'que preenche o campo senha em branco')
def step_impl(context):
    nlcp.escrever_senha('')

@given(u'que preenche o campo senha invalida')
def step_impl(context):
    nlcp.escrever_senha('1234')

@given(u'que preenche o campo confirme a senha em branco')
def step_impl(context):
    nlcp.confirmar_senha('')

@given(u'que preenche o campo confirme a senha invalida')
def step_impl(context):
    nlcp.confirmar_senha('1342')

@given(u'que preenche o campo confirme a senha')
def step_impl(context):
    nlcp.confirmar_senha('123456')

@given(u'que preenche o campo e-mail')
def step_impl(context):
    nlcp.escrever_email(sup.mask_email_generator())

@when(u'clico no botão cadastrar')
def step_impl(context):
    nlcp.clicar_cadastro()

@then(u'devo passar para o preenchimento dos próximos dados')
def step_impl(context):
    assert nlcp.driver.title != 'Atualização de Usuário'

@then(u'devo falhar no cadastro')
def step_impl(context):
    assert nlcp.driver.find_element(By.ID, "id_error_display_fixed") in nlcp.driver.current_window_handle

@given(u'que acessa a seção de cadastro da página NL em específico o campo de email')
def step_impl(context):
    nlcp.acessar_Nl('https://prpi.ifce.edu.br/nl/app_form_add_users/')

@given(u'que preenche o campo e-mail em branco')
def step_impl(context):
    nlcp.escrever_email('')

@given(u'que preenche o campo e-mail inválido')
def step_impl(context):
    nlcp.escrever_email('12345677777')

@then(u'devo passar para o preenchimento dos próximos dados')
def step_impl(context):
    nlcp.escrever_email(sup.mask_email_generator)
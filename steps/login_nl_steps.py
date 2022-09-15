from time import sleep
from behave import *
from pages.login_nl_page import NLLoginPage

nlLoginPage = NLLoginPage()

@given(u'que acesso a página do NL')
def step_impl(context):
    nlLoginPage.acessar_Nl("https://prpi.ifce.edu.br/nl")

@given(u'que preencho o campo cpf')
def step_impl(context):
    nlLoginPage.escrever_cpf('...')

@given(u'que preencho o campo senha')
def step_impl(context):
    nlLoginPage.escrever_senha('...')

@when(u'clico no botão entrar')
def step_impl(context):
    nlLoginPage.clicar_acessar()
    sleep(2)

@then(u'devo logar no sistema')
def step_impl(context):
    assert nlLoginPage.driver.title == 'Menu Principal'
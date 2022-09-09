from behave import *
from pages.login_sei_page import NLLoginPage

nlLoginPage = NLLoginPage()

@given(u'que acesso a página do NL')
def step_impl(context):
    nlLoginPage.acessar_Nl("https://prpi.ifce.edu.br/nl")


@given(u'que preencho o campo cpf')
def step_impl(context):
    nlLoginPage.escrever_cpf('12312312312')


@given(u'que preencho o campo senha')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que preencho o campo senha')


@when(u'clico no botão entrar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão entrar')


@then(u'devo logar no sistema')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo logar no sistema')

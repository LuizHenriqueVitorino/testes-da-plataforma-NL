from behave import *

from login import Login
from pages.login_nl_page import NLLoginPage
from selenium.webdriver.common.by import By

nlcp = NLLoginPage()
obj_login = Login()

@given(u'que acesso a página do NL')
def step_impl(context):
    nlcp.acessar_Nl("https://prpi.ifce.edu.br/nl")

@given(u'que preencho o campo cpf')
def step_impl(context):
    nlcp.escrever_cpf(obj_login.CPF)

@given(u'que preencho o campo senha')
def step_impl(context):
    nlcp.escrever_senha(obj_login.SENHA)

@when(u'clico no botão entrar')
def step_impl(context):
    nlcp.clicar_acessar()

@then(u'devo logar no sistema')
def step_impl(context):
    assert nlcp.driver.find_element(By.ID, "lin2_col1").text == 'Plataforma NL'
    assert nlcp.driver.title == 'Menu Principal'
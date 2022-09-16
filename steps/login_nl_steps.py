from time import sleep
from behave import *
from pages.login_nl_page import NLLoginPage, NLLoginPageLocator
from selenium.webdriver.common.by import By

nlLoginPage = NLLoginPage()
nlLocator   = NLLoginPageLocator()

@given(u'que acesso a página do NL')
def step_impl(context):
    nlLoginPage.acessar_Nl("https://prpi.ifce.edu.br/nl")

@given(u'que preencho o campo cpf')
def step_impl(context):
    nlLoginPage.escrever_cpf('60435252321')

@given(u'que preencho o campo senha')
def step_impl(context):
    nlLoginPage.escrever_senha('147896325')

@when(u'clico no botão entrar')
def step_impl(context):
    nlLoginPage.clicar_acessar()

@then(u'devo logar no sistema')
def step_impl(context):
    assert nlLoginPage.driver.find_element(By.ID, nlLocator.ID_PLATAFORMA_NL).text == "Plataforma NL"
    assert nlLoginPage.driver.title == 'Menu Principal'
from behave import *
from pages.login_nl_page import NLLoginPage
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nlLoginPage = NLLoginPage()
browser_driver = Browser()

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

@then(u'devo logar no sistema')
def step_impl(context):
    assert browser_driver.driver.title == 'Menu Principal'
from ast import Assert
from behave import *
from login import Login
from pages.pesquisador_nl_page import NLPesquisadorPage
from selenium.webdriver.common.by import By

obj_login = Login()
obj_pesquisador = NLPesquisadorPage()

@given(u'que realiza o login do usuário')
def step_impl(context):
    obj_login.acessar_Nl('https://prpi.ifce.edu.br/nl/app_Login/')
    obj_login.logar()


@given(u'que acessa alterar seus dados')
def step_impl(context):
    obj_pesquisador.acessar_alterar_dados()
    obj_pesquisador.clicar_branco()


@then(u'o titulo da aba deve ser igual ao do menu')
def step_impl(context):
    assert obj_login.CPF in obj_pesquisador.driver.find_element(By.ID, 'lin1_col2').text
    # assert obj_pesquisador.driver.find_element(By.ID, 'aba_td_item_5').text == 'Alterar seus Dados'
    # obj_pesquisador.driver.find_element(By.ID, 'item_5')
    obj_pesquisador.fechar_aba(fechar_alterar_dados=True)
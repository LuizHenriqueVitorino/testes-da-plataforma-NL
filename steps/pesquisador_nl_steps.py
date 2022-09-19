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

@then(u'o campo cpf deve ser igual ao de login')
def step_impl(context):
    assert 'Alterar seus Dados' == obj_pesquisador.driver.find_element(By.ID,'aba_td_item_5').text
    obj_pesquisador.driver.switch_to.frame("iframe_item_5") # Muda para o frame que contem os dados 
    assert obj_pesquisador.driver.find_element(By.ID, 'id_read_on_cpf').text == obj_login.CPF
    obj_pesquisador.driver.switch_to.parent_frame() # Volta para o frame original
    obj_pesquisador.fechar_aba(fechar_alterar_dados=True)
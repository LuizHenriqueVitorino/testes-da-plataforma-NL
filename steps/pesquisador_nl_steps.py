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
    obj_pesquisador.driver.switch_to.frame('iframe_item_5') #TODO Muda para o frame que contem os dados 
    assert obj_pesquisador.driver.find_element(By.ID, 'id_read_on_cpf').text == obj_login.CPF
    obj_pesquisador.driver.switch_to.parent_frame() #TODO Volta para o frame original
    obj_pesquisador.fechar_aba(fechar_alterar_dados=True)

@given(u'que acessa alterar senha')
def step_impl(context):
    obj_pesquisador.acessar_alterar_senha()
    obj_pesquisador.clicar_branco()

@given(u'preenche os campos de senha de forma correta')
def step_impl(context):
    obj_pesquisador.driver.switch_to.frame('iframe_item_12')
    obj_pesquisador.alterar_senha(nova_senha='123456', confirme_nova_senha='123456')
    obj_pesquisador.driver.switch_to.parent_frame()

@then(u'a senha deve ser alterada')
def step_impl(context):
    assert 'Plataforma NL da PRPI' in obj_pesquisador.driver.find_element(By.XPATH, '//div/h1').text
    assert obj_pesquisador.driver.title == 'Login PNL'

@given(u'preenche os campos de senha e confirme senha de forma incorreta')
def step_impl(context):
    obj_pesquisador.driver.switch_to.frame('iframe_item_12')
    obj_pesquisador.alterar_senha(nova_senha='123', confirme_nova_senha='123')
    
@then(u'a senha devo falhar na alteração das senhas')
def step_impl(context):
    assert 'ERROR' in obj_pesquisador.driver.find_element(By.ID, 'id_error_display_fixed').text
    obj_pesquisador.driver.switch_to.parent_frame()
    obj_pesquisador.fechar_aba(fechar_alterar_senha=True)

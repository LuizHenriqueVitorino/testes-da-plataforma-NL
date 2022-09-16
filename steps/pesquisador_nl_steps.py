from behave import *
from login import Login
from pages.pesquisador_nl_page import NLPesquisadorPage

obj_login = Login()
obj_pesquisador = NLPesquisadorPage()

@given(u'que realiza o login do usuário')
def step_impl(context):
    obj_login.acessar_Nl('https://prpi.ifce.edu.br/nl/app_Login/')
    obj_login.logar()


@given(u'que acessa alterar seus dados')
def step_impl(context):
    obj_pesquisador.acessar_alterar_dados()


@then(u'o titulo da aba deve ser igual ao do menu')
def step_impl(context):
    pass
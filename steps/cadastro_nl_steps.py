from behave import *
# from pages.cadastro_nl_page import NLCadastroPage as NLCP
from browser import Browser

@given(u'que acessa a seção de cadastro da página NL')
def step_impl(context):
    # NLPC.nl_cadastro(context.url)
    pass
@given(u'que preenche o campo cpf')
def step_impl(context):
    # NLPC.nl_escrever_cpf(cpf)
    pass
@given(u'que preenche o campo cpf com branco')
def step_impl(context):
    # NLPC.nl_escrever_cpf(''/ pode ser um boolean em falso para preencher com branco)
    pass
@given(u'que preenche o campo senha')
def step_impl(context):
    # NLPC.nl_escrever_senha(senha)
    pass
@given(u'que preenche o campo confirme a senha')
def step_impl(context):
    # NLPC.nl_escrever_confirme_senha(senha)
    pass
@given(u'que preenche o campo e-mail')
def step_impl(context):
    # NLPC.nl_escrever_email(email)
    pass
@when(u'clico no botão cadastrar')
def step_impl(context):
    # NLPC.nl_clicar_cadastrar()
    pass
@then(u'devo passar para o preenchimento dos próximos dados')
def step_impl(context):
    # assert Browser.driver.title == 'Inclusão - nl_Pessoa'
    pass

@then(u'devo falhar no cadastro')
def step_impl(context):
    # assert Browser.driver.title != 'Inclusão - nl_Pessoa'
    pass
    
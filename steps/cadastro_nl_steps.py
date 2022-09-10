from behave import *
# from pages.cadastro_nl_page import NLCadastroPage as NLCP

@given(u'que acessa a seção de cadastro da página NL')
def step_impl(context):
    context.url = 'https://prpi.ifce.edu.br/nl/app_form_add_users/'
    # NLPC.nl_cadastro(context.url)
    pass
@given(u'que preenche o campo cpf')
def step_impl(context):
    # NLPC.nl_escrever_cpf(cpf)
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
    assert context.url != 'https://prpi.ifce.edu.br/nl/form_nl_Pessoa/'
    
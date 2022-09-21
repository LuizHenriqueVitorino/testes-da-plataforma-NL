from pages.login_nl_page import NLLoginPage

class Login(NLLoginPage):
    #TODO antes de qualquer teste preencha as constantes
    CPF = ''
    SENHA = ''
    obj_login_page = NLLoginPage()

    def logar(self):
        self.obj_login_page.escrever_cpf(self.CPF)
        self.obj_login_page.escrever_senha(self.SENHA)
        self.obj_login_page.clicar_acessar()
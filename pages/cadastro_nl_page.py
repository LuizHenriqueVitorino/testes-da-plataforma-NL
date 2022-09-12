from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser


class NLCadastroPageLocator(object):
    # TODO Escrever os locators necessários para realizar o login na pagina NL
    INPUT_CPF = "id_sc_field_login"
    INPUT_SENHA = "id_sc_field_pswd"
    INPUT_CONFIRMA_SENHA = "id_sc_field_confirm_pswd"
    INPUT_EMAIL = "id_sc_field_email"
    INPUT_CADASTRAR = "//span[.='Cadastrar']"


class NLCadastroPage(Browser):
    # def escrever_email(self):
    # TODO Escreve as funções da page. Para os meninos do teste...

    def acessar_Nl(self, url):
        self.driver.get(url)

    def escrever_cpf(self, cpf):
        inputCPF = self.driver.find_element(
            By.ID, NLCadastroPageLocator.INPUT_CPF)
        inputCPF.send_keys(cpf)

    def escrever_senha(self, senha):
        input_senha = self.driver.find_element(
            By.ID, NLCadastroPageLocator.INPUT_SENHA)
        input_senha.send_keys(senha)

    

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class NLLoginPageLocator(object):
    # TODO Escrever os locators necessários para realizar o login na pagina NL
    INPUT_CPF = "id_sc_field_login"
    INPUT_SENHA = "id_sc_field_pswd"
    CLICK_ACESSAR = "//div/input[@class='button']"

class NLLoginPage(Browser):

    def acessar_Nl(self, url):
        self.driver.get(url)

    def escrever_cpf(self, cpf):
        inputCPF = self.driver.find_element(By.ID, NLLoginPageLocator.INPUT_CPF)
        inputCPF.send_keys(cpf)

    def escrever_senha(self, senha): 
        input_senha = self.driver.find_element(By.ID, NLLoginPageLocator.INPUT_SENHA)
        input_senha.send_keys(senha)
    
    def clicar_acessar(self):
        clicar = self.driver.find_element(By.XPATH,NLLoginPageLocator.CLICK_ACESSAR)
        clicar.click()
        
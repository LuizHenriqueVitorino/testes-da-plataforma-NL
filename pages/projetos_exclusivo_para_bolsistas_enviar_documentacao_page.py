from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from login import Login

login = Login()

class NLExclusivoParaBolsistasEnviarDocumetacaoLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    XPATH_EXCLUSIVO_PARA_BOLSISTAS = "//a/span[.='Exclusivo para Bolsistas']"
    ID_ENVIAR_DOCUMENTACAO = "item_65"
    ID_ASSERT_ENVIAR_DOCUMENTACAO = "aba_td_txt_item_65"
    ID_FECHAR_ABA_ENVIAR_DOCUMENTACAO = "aba_td_img_item_65"

class NLExclusivoParaBolsistasEnviarDocumentacao(Browser):
    login.logar

    def acessar_aba_projetos(self):
        projetos = self.driver.find_element(
            By.XPATH, NLExclusivoParaBolsistasEnviarDocumetacaoLocator.XPATH_PROJETOS) 
        projetos.click()

    def acessar_aba_exclusivo_para_bolsistas(self):
        exclusivo_para_bolsistas = self.driver.find_element(
            By.XPATH, NLExclusivoParaBolsistasEnviarDocumetacaoLocator.XPATH_EXCLUSIVO_PARA_BOLSISTAS)
        exclusivo_para_bolsistas.click()

    def acessar_aba_enviar_documentacao(self):
        enviar_documentacao = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarDocumetacaoLocator.ID_ENVIAR_DOCUMENTACAO)
        enviar_documentacao.click()

    def procurar_enviar_documentacao(self):
        assert_no_enviar_documentacao = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarDocumetacaoLocator.ID_ASSERT_ENVIAR_DOCUMENTACAO)
        assert assert_no_enviar_documentacao.text == "Enviar Documentação"

    def fechar_aba_enviar_documentacao(self):
        fechar_aba_enviar_documentacao = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarDocumetacaoLocator.ID_FECHAR_ABA_ENVIAR_DOCUMENTACAO)
        fechar_aba_enviar_documentacao.click()




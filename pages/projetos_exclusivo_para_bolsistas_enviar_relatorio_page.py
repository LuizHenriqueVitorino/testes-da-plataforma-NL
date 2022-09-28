from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from login import Login

login = Login()

class NLExclusivoParaBolsistasEnviarRelatorioLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    XPATH_EXCLUSIVO_PARA_BOLSISTAS = "//a/span[.='Exclusivo para Bolsistas']"
    ID_ENVIAR_RELATORIO = "item_70"
    ID_ASSERT_ENVIAR_RELATORIO = "aba_td_txt_item_70"
    ID__CLICAR_PLATAFORMA_NL = "lin2_col1"
    ID_FECHAR_ABA_ENVIAR_RELATORIO = "aba_td_img_item_70"

class NLExclusivoParaBolsistasEnviarRelatorio(Browser):
    login.logar

    def acessar_aba_projetos(self):
        projetos = self.driver.find_element(
            By.XPATH, NLExclusivoParaBolsistasEnviarRelatorioLocator.XPATH_PROJETOS) 
        projetos.click()

    def acessar_aba_exclusivo_para_bolsistas(self):
        exclusivo_para_bolsistas = self.driver.find_element(
            By.XPATH, NLExclusivoParaBolsistasEnviarRelatorioLocator.XPATH_EXCLUSIVO_PARA_BOLSISTAS)
        exclusivo_para_bolsistas.click()

    def acessar_enviar_relatorio(self):
        enviar_relatorio = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarRelatorioLocator.ID_ENVIAR_RELATORIO)
        enviar_relatorio.click()

    def procurar_enviar_relatorio(self):
        assert_no_enviar_relatorio = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarRelatorioLocator.ID_ASSERT_ENVIAR_RELATORIO)
        assert assert_no_enviar_relatorio.text == "Enviar Relatório"

    def clicar_na_plataforma_NL(self):
        clicar_plataforma_nl = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarRelatorioLocator.ID__CLICAR_PLATAFORMA_NL)
        clicar_plataforma_nl.click()

    def fechar_aba_enviar_relatorio(self):
        fechar_a_aba_enviar_relatorio = self.driver.find_element(
            By.ID, NLExclusivoParaBolsistasEnviarRelatorioLocator.ID_FECHAR_ABA_ENVIAR_RELATORIO)
        fechar_a_aba_enviar_relatorio.click()


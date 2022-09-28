from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from login import Login

login = Login()

class NLListarEmExecucaoEExecutadosLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    ID_LISTAR_EM_EXECUCAO_E_EXECUTADOS = "item_13"
    ID_ASSERT_LISTAR_EM_EXECUCAO_E_EXECUTADOS = "aba_td_txt_item_13"
    ID__CLICAR_PLATAFORMA_NL = "lin2_col1"
    ID_FECHAR_ABA_LISTAR_EM_EXECUCAO_E_EXECUTADOS = "aba_td_img_item_13"

class NLListarEmExecucaoEExecutados(Browser):
    login.logar

    def acessar_aba_projetos(self):
        projetos = self.driver.find_element(
            By.XPATH, NLListarEmExecucaoEExecutadosLocator.XPATH_PROJETOS) 
        projetos.click()

    def acessar_listar_em_execucao_e_executados(self):
        listar_em_execucao_e_executados = self.driver.find_element(
            By.ID, NLListarEmExecucaoEExecutadosLocator.ID_LISTAR_EM_EXECUCAO_E_EXECUTADOS)
        listar_em_execucao_e_executados.click()

    def procurar_listar_em_execucao_e_executados(self):
        assert_no_id_listar_em_execucao_e_executados = self.driver.find_element(
            By.ID, NLListarEmExecucaoEExecutadosLocator.ID_ASSERT_LISTAR_EM_EXECUCAO_E_EXECUTADOS)
        assert assert_no_id_listar_em_execucao_e_executados.text == "Listar em execução e executados"

    def clicar_na_plataforma_NL(self):
        clicar_plataforma_nl = self.driver.find_element(
            By.ID, NLListarEmExecucaoEExecutadosLocator.ID__CLICAR_PLATAFORMA_NL)
        clicar_plataforma_nl.click()

    def fechar_aba_listar_em_execucao_e_executados(self):
        fechar_a_aba_listar_em_execucao_e_executados = self.driver.find_element(
            By.ID, NLListarEmExecucaoEExecutadosLocator.ID_FECHAR_ABA_LISTAR_EM_EXECUCAO_E_EXECUTADOS)
        fechar_a_aba_listar_em_execucao_e_executados.click()

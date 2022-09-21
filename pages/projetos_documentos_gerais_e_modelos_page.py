from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from login import Login

login = Login()


class NLDocumentosGeraisEModelosLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    ID_DOCUMENTOS_GERAIS_E_MODELOS = "item_136"
    ID_ASSERT_DOCUMENTOS_GERAIS_E_MODELOS = "aba_td_txt_item_136"
    ID__CLICAR_PLATAFORMA_NL = "lin2_col1"
    ID_FECHAR_ABA_DOCUMENTOS_GERAIS_E_MODELOS = "aba_td_img_item_136"


class NLDocumentosGeraisEModelos(Browser):
    login.logar

    def acessar_aba_projetos(self):
        projetos = self.driver.find_element(
            By.XPATH, NLDocumentosGeraisEModelosLocator.XPATH_PROJETOS) 
        projetos.click()

    def acessar_doc_gerais_e_modelos(self):
        documentos_gerais_e_modelos = self.driver.find_element(
            By.ID, NLDocumentosGeraisEModelosLocator.ID_DOCUMENTOS_GERAIS_E_MODELOS)
        documentos_gerais_e_modelos.click()

    def procurar_documentos_na_pag(self):
        assert_no_id_documentos = self.driver.find_element(
            By.ID, NLDocumentosGeraisEModelosLocator.ID_ASSERT_DOCUMENTOS_GERAIS_E_MODELOS)
        assert assert_no_id_documentos.text == "Documentos Gerais e Modelos"

    def clicar_na_plataforma_NL(self):
        clicar_plataforma_nl = self.driver.find_element(
            By.ID, NLDocumentosGeraisEModelosLocator.ID__CLICAR_PLATAFORMA_NL)
        clicar_plataforma_nl.click()
    
    def fechar_doc_gerais_e_modelos(self):
        fechar_aba_documentos_gerais_e_modelos = self.driver.find_element(
            By.ID, NLDocumentosGeraisEModelosLocator.ID_FECHAR_ABA_DOCUMENTOS_GERAIS_E_MODELOS)
        fechar_aba_documentos_gerais_e_modelos.click()
        

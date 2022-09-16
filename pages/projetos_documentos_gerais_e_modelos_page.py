from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class NLDocumentosGeraisEModelosLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    ID_DOCUMENTOS_GERAIS_E_MODELOS = "item_136"
    ID_ASSERT_DOCUMENTOS_GERAIS_E_MODELOS = "aba_td_txt_item_136"
    ID_FECHAR_ABA_DOCUMENTOS_GERAIS_E_MODELOS = "aba_td_img_item_136"

class NLDocumentosGeraisEModelos(Browser):
    pass


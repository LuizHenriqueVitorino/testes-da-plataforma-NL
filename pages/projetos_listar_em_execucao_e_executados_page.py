from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class NLListarEmExecucaoEExecutadosLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    ID_LISTAR_EM_EXECUCAO_E_EXECUTADOS = "item_13"
    ID_ASSERT_LISTAR_EM_EXECUCAO_E_EXECUTADOS = "aba_td_txt_item_13"
    ID_FECHAR_ABA_LISTAR_EM_EXECUCAO_E_EXECUTADOS = "aba_td_img_item_13"

class NLListarEmExecucaoEExecutados(Browser):
    pass

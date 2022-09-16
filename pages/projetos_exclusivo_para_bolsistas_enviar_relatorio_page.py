from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class NLExclusivoParaBolsistasEnviarRelatorioLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    XPATH_EXCLUSIVO_PARA_BOLSISTAS = "//a/span[.='Exclusivo para Bolsistas']"
    ID_ENVIAR_RELATORIO = "item_70"
    ID_ASSERT_ENVIAR_RELATORIO = "aba_td_txt_item_70"
    ID_FECHAR_ABA_ENVIAR_RELATORIO = "aba_td_img_item_70"

class NLExclusivoParaBolsistasEnviarRelatorio(Browser):
    pass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class NLListarTodosOsSeusProjetosLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    ID_LISTAR_TODOS_OS_SEUS_PROJETOS = "item_130"
    ID_ASSERT_LISTAR_TODOS_OS_SEUS_PROJETOS = "aba_td_txt_item_130"
    ID_FECHAR_ABA_LISTAR_TODOS_OS_SEUS_PROJETOS = "aba_td_img_item_130"

class NLListarTodosOsSeusProjetos(Browser):
    pass

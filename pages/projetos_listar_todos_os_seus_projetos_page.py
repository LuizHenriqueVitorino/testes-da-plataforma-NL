from gettext import find
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from login import Login

login = Login()

class NLListarTodosOsSeusProjetosLocator(object):
    XPATH_PROJETOS = "//span[.=' Projetos']"
    ID_LISTAR_TODOS_OS_SEUS_PROJETOS = "item_130"
    ID_ASSERT_LISTAR_TODOS_OS_SEUS_PROJETOS = "aba_td_txt_item_130"
    ID_FECHAR_ABA_LISTAR_TODOS_OS_SEUS_PROJETOS = "aba_td_img_item_130"

class NLListarTodosOsSeusProjetos(Browser):
    login.logar

    def acessar_aba_projetos(self):
        projetos = self.driver.find_element(
            By.XPATH, NLListarTodosOsSeusProjetosLocator.XPATH_PROJETOS) 
        projetos.click()

    def acessar_todos_os_seus_projetos(self):
        listar_todos_os_seus_projetos = self.driver.find_element(
            By.ID, NLListarTodosOsSeusProjetosLocator.ID_LISTAR_TODOS_OS_SEUS_PROJETOS)
        listar_todos_os_seus_projetos.click()

    def procurar_listar_todos_os_seus_projetos(self):
        assert_no_listar_todos_os_seus_projetos = self.driver.find_element(
            By.ID, NLListarTodosOsSeusProjetosLocator.ID_ASSERT_LISTAR_TODOS_OS_SEUS_PROJETOS)
        assert assert_no_listar_todos_os_seus_projetos.text == "Listar todos os seus projetos"

    def fechar_aba_listar_todos_os_seus_projetos(self):
        fechar_a_aba_listar_todos_os_seus_projetos = self.driver.find_element(
            By.ID, NLListarTodosOsSeusProjetosLocator.ID_FECHAR_ABA_LISTAR_TODOS_OS_SEUS_PROJETOS)
        fechar_a_aba_listar_todos_os_seus_projetos.click()
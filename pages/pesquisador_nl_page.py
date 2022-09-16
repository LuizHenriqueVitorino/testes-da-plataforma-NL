from selenium.webdriver.common.by import By
from browser import Browser


class NLPesquisadorPageLocator(object):
    ID_PESQUISADOR = 'item_4'
    ID_ALTERAR_DADOS = 'item_5'
    ID_FECHAR_ALTERAR_DADOS = 'aba_td_img_item_item_5'
    ID_ALTERAR_SENHA = 'item_12'
    ID_FECHAR_ALTERAR_SENHA = 'aba_td_img_item_item_12'
    ID_MENSAGEM_SISTEMA = 'item_58'
    ID_FECHAR_MENSAGEM_SISTEMA = 'aba_td_img_item_item_58'
    ID_CONVERSOR_LATTES = 'item_128'
    ID_SEUS_NUMEROS = 'item_54'
    ID_DASHBOARD = 'item_66'
    ID_FECHAR_DASHBOARD = 'aba_td_img_item_item_66'

class NLPesquisadorPage(Browser):
    
    def acessar_alterar_dados(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
        alterar_dados = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_ALTERAR_DADOS)
        alterar_dados.click()

    def acessar_alterar_senha(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
        alterar_senha = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_ALTERAR_SENHA)
        alterar_senha.click()

    def acessar_mensagem_sistema(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
        mensagem_sistema = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_MENSAGEM_SISTEMA)
        mensagem_sistema.click()

    def acessar_conversor_lattes(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
        conversor_lattes = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_CONVERSOR_LATTES)
        conversor_lattes.click()
        
    def acessar_conversor_lattes(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
        conversor_lattes = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_CONVERSOR_LATTES)
        conversor_lattes.click()
        
    def acessar_dashoard(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
        seus_numeros = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_SEUS_NUMEROS)
        seus_numeros.click()
        dashboard = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_DASHBOARD)
        dashboard.click()
        
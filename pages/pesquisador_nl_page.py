from selenium.webdriver.common.by import By
from browser import Browser
from login import Login

class NLPesquisadorPageLocator(object):
    ID_PESQUISADOR = 'item_4'
    ID_ALTERAR_DADOS = 'item_5'
    ID_FECHAR_ALTERAR_DADOS = 'aba_td_img_item_5'
    ID_ALTERAR_SENHA = 'item_12'
    ID_FECHAR_ALTERAR_SENHA = 'aba_td_img_item_12'
    ID_MENSAGEM_SISTEMA = 'item_58'
    ID_FECHAR_MENSAGEM_SISTEMA = 'aba_td_img_item_58'
    ID_CONVERSOR_LATTES = 'item_128'
    ID_SEUS_NUMEROS = 'item_54'
    ID_DASHBOARD = 'item_66'
    ID_FECHAR_DASHBOARD = 'aba_td_img_item_66'
    ID_ESPAÇO_BRANCO = 'lin1_col2'
    ID_SENHA_ANTIGA = 'id_sc_field_old_pswd'
    ID_SENHA = 'id_sc_field_pswd'
    ID_CONFIRME_SENHA = 'id_sc_field_confirm_pswd'
    ID_OK_ALTERAR_SENHA = 'sub_form_b'
    XPATH_DETALHES_MENSAGENS_SISTEMA = '//tr[@id="SC_ancor1"]/td/table/tbody/tr/td/a'

class NLPesquisadorPage(Browser):

    obj_login = Login()

    def clicar_branco(self):
        self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_ESPAÇO_BRANCO).click()

    def pesquisador(self):
        pesquisador = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_PESQUISADOR)
        pesquisador.click()
    
    def acessar_alterar_dados(self):
        self.pesquisador()
        alterar_dados = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_ALTERAR_DADOS)
        alterar_dados.click()

    def acessar_alterar_senha(self):
        self.pesquisador()
        alterar_senha = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_ALTERAR_SENHA)
        alterar_senha.click()

    def acessar_mensagem_sistema(self):
        self.pesquisador()
        mensagem_sistema = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_MENSAGEM_SISTEMA)
        mensagem_sistema.click()

    def acessar_conversor_lattes(self):
        self.pesquisador()
        conversor_lattes = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_CONVERSOR_LATTES)
        conversor_lattes.click()
        
    def acessar_dashoard(self):
        self.pesquisador()
        seus_numeros = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_SEUS_NUMEROS)
        seus_numeros.click()
        dashboard = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_DASHBOARD)
        dashboard.click()

    def fechar_aba(self, fechar_alterar_dados=False, fechar_alterar_senha=False, fechar_mensagem_sistema=False, fechar_dashboard=False):
        if fechar_alterar_dados:
            self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_FECHAR_ALTERAR_DADOS).click()
        if fechar_alterar_senha:
            self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_FECHAR_ALTERAR_SENHA).click()
        if fechar_mensagem_sistema:
            self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_FECHAR_MENSAGEM_SISTEMA).click()
        if fechar_dashboard:
            self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_FECHAR_DASHBOARD).click()
    
    def alterar_senha(self, nova_senha, confirme_nova_senha):
        senha_antiga = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_SENHA_ANTIGA)
        senha_antiga.send_keys(self.obj_login.SENHA)
        senha = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_SENHA)
        senha.send_keys(nova_senha)
        confirme_senha = self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_CONFIRME_SENHA)
        confirme_senha.send_keys(confirme_nova_senha)
        self.driver.find_element(By.ID, NLPesquisadorPageLocator.ID_OK_ALTERAR_SENHA).click()

    def acessar_detalhes_mensagens(self):
        self.driver.find_element(By.XPATH, NLPesquisadorPageLocator.XPATH_DETALHES_MENSAGENS_SISTEMA).click()
                      
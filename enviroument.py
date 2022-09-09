from browser import Browser

# Execulta os comandos antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()

# Execulta os comandos antes de todos os testes iniciarem
def after_all(context):
    context.browser.browser.quit()

# Execulta os comandos entre cada cenário
def after_scenario(context, scenario):
    context.browser.browser_clear()

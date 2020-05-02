import time
from selenium.webdriver import Firefox

browser = Firefox()

#from selenium.webdriver import Chrome
#browser = Chrome()

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)
time.sleep(3)

h1 = browser.find_element_by_tag_name('h1')
paragrafos = browser.find_elements_by_tag_name('p')

p_dicionario = {}

for p in paragrafos:
    p_dicionario.update(
        {p.get_attribute('atributo'): p.text}
    )
   

dicionario_de_atributos = {
    h1.text:p_dicionario
}

print(dicionario_de_atributos)

browser.quit()
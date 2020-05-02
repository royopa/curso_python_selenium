import time
from selenium.webdriver import Firefox

browser = Firefox()

#from selenium.webdriver import Chrome
#browser = Chrome()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
time.sleep(3)

xpath = '/html/body/p[2]'
numero_esperado = browser.find_element_by_xpath(xpath).text
numero_esperado = numero_esperado.split('Numero esperado: ')[1]
print(f'Meu número esperado é {numero_esperado}')

link_para_clicar = browser.find_element_by_tag_name('a')

p = browser.find_element_by_tag_name('p')

continua = True

while continua is True:
    link_para_clicar.click()
    p = browser.find_elements_by_tag_name('p')[-1]
    numero_gerado = p.text

    if 'Você ganhou: ' in p.text:
        numero_gerado = p.text.split('Você ganhou: ')[1]
    
    numero_gerado = int(numero_gerado)
    
    print(f'Número gerado: {numero_gerado} - Número esperado: {numero_esperado} - São iguais? {int(numero_esperado) == numero_gerado}')

    if int(numero_esperado) == numero_gerado:
        print('Saindo')
        continua = False


#browser.quit()
import time
from selenium.webdriver import Firefox
import pyautogui

'''
import webbrowser
import os
import fnmatch
import shutil


webbrowser.open(url)


'''

url = 'https://economatica.com/'
browser = Firefox()
browser.get(url)
time.sleep(5)

browser.find_element_by_id('modalLink').click()
time.sleep(5)

## You have to switch to the iframe like so: ##
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))

browser.find_element_by_id('ecoUser').send_keys('usuario')
browser.find_element_by_id('ecoPasswd').send_keys('senha')

xpath='/html/body/center/div/table/tbody/tr[3]/td/div/form/table/tbody/tr[5]/td[2]/input'
browser.find_element_by_xpath(xpath).click()

## Switch back to the "default content" (that is, out of the iframes) ##
browser.switch_to.default_content()
# time.sleep(120)

'''
print('Clica no botão fechar do Economatica')
print(pyautogui.position())
pyautogui.click(x=1750, y=305)

print('Clica no botão para abrir tela pré-gravada')
print(pyautogui.position())
pyautogui.click(x=801, y=155)
time.sleep(3)

print('Clica no botão para abrir o arquivo BOVESPA da GERAT')
print(pyautogui.position())
pyautogui.click(x=1128, y=637)
time.sleep(1)

print('Clica no botão abrir')
pyautogui.click(x=1431, y=852)
time.sleep(1)


pyautogui.click(x=1328, y=208)
pyautogui.click(x=1201, y=301)
pyautogui.click(x=1067, y=457)
pyautogui.click(x=856, y=633)
pyautogui.click(x=706, y=735)

print('Clica no botão exportar')
pyautogui.click(x=798, y=822)
'''

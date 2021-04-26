# POR 'ID' ##

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_05_a.html"
#entrando na url
driver.get(url)

#encontrando o elemento por id
div_py = driver.find_element_by_id('python')
div_hk = driver.find_element_by_id('haskell')

print(div_hk.text)

driver.quit()


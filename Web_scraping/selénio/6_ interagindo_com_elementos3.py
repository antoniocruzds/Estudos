# POR 'NAME' ## / DIGITANDO NA PAG

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_05_c.html"
#entrando na url
driver.get(url)
'''
#encontraremos os elementos por nome e depois preencheremos
filme = driver.find_element_by_name('filme')
filme.send_keys('Parasita') #preenchendo com parasita

email = driver.find_element_by_name('email')
email.send_keys('antoniocruznb@gmail.com')#preenchendo email

telefone = driver.find_element_by_name('telefone')
telefone.send_keys('(071)987654321')#preenchendo email

#para clicar
driver.find_element_by_name('enviar').click()

'''
#por uma função:

def melhor_filme(driver, filme, email, telefone):
    driver.find_element_by_name('filme').send_keys(filme)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('telefone').send_keys(telefone)
    driver.find_element_by_name('enviar').click()

melhor_filme(driver, 'parasita', 'antoniocruznb@gmail.com', '(071)987654321')
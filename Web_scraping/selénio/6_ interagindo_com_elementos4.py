# POR 'NAME' ## / DIGITANDO NA PAG

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_05.html"
#entrando na url
driver.get(url)
sleep(3)

#names: nome, email, senha, telefone, btn

#por função:
def preenche_form(driver, nome, email, senha, telefone):
    driver.find_element_by_name('nome').send_keys(nome)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('senha').send_keys(senha)
    driver.find_element_by_name('telefone').send_keys(telefone)
    driver.find_element_by_name('btn').click()

preenche_form(driver, 'neto', 'antoniocruznb@gmail.com', '123456789', '(071)987654321')
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#Vamos criar uma função para achar o texto:
"""
Encontrar o elemento com o texto 'text'
Argumentos:
    - driver = browser usado (chrome)
    - text = conteudo que deve estar na tag
    - tag = tag onde o texto será procurado
"""

def find_by_text(driver, tag, text):
    elementos1 = driver.find_elements_by_tag_name(tag) #lista
    for elemento in elementos1:
        if elemento.text == text:
            return elemento

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_04_b.html"
#entrando na url
driver.get(url)

#definindo o nome das caixas e entrando nelas
nome_das_caixas = ['um', 'dois', 'tres', 'quatro']
for nome in nome_das_caixas:
    find_by_text(driver, 'div', nome).click()

for nome in nome_das_caixas:
    sleep(0.4) #esperando um segundo
    driver.back() #voltando uma casa 

for nome in nome_das_caixas:
    sleep(0.4) #esperando um segundo
    driver.forward() #avançando uma casa
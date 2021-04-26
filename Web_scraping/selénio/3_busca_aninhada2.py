# BUSCANDO POR ATRIBUTOS #

from selenium import webdriver
from time import sleep

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

#Vamos criar uma função para achar o link (href):
"""
Encontrar o elemento 'a' com o link 'href'
Argumentos:
    - driver = browser usado (chrome)
    - link = link que sera procurado na tag 'a'
"""

def find_by_href(driver, link):
    elementos2 = driver.find_elements_by_tag_name('a') #lista

    for elemento in elementos2:
        if link in elemento.get_attribute('href'):
            return elemento


driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_04_a.html"
#entrando na url
driver.get(url)

#usando as funções criadas
elemento_ddg = find_by_text(driver, 'li', 'DuckDuckGo')
elemento_ddg_link = find_by_href(driver, 'ddg')

link = elemento_ddg_link.get_attribute('href')

print(f'o texto do elemento é:  {elemento_ddg.text}')
print(f'o link do elemento é:  {link}')

#fechando o navegador
driver.quit()
 # -------------------------------- #
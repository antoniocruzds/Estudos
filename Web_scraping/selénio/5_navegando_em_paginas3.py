"""
1. pegar todos os links das aulas:
    {'nome da aula': 'link da aula'}
2. Navegar até o exercicio 3
    achar a url do exercicio e entrar nela
"""

from selenium import webdriver
from time import sleep
from urllib.parse import urlparse
from pprint import pprint

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_04.html"
#entrando na url
driver.get(url)

url_parseada = urlparse(driver.current_url)
print(url_parseada) #mostra as partes da url
sleep(2)

"""
parte 1
"""
# Normal
"""
aside = driver.find_element_by_tag_name('aside')
aside_acoras = aside.find_elements_by_tag_name('a')

resultado_1 = {}

for acora in aside_acoras:
    resultado_1[acora.text] = acora.get_attribute('href')

pprint(resultado_1)

driver.get(resultado_1['Aula 3']) #ir para uma página no dicionario
"""
#Por função
#criando uma função:
def get_links(driver, elemento):
    """
    pega todos os links em um elemento

    - driver = instancia do navegador
    - element = webelement [aside, mais, body...]
    """
    resultado = {}
    element = driver.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for acora in ancoras:
        resultado[acora.text] = acora.get_attribute('href')
    return resultado

pprint(get_links(driver, 'aside'))

"""
Parte 2
"""
exercicios = get_links(driver, 'main')
pprint(exercicios)

driver.get(exercicios['Exercício 3'])
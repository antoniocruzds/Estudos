# BuSCANDO POR ELEMENTOS #

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_04_a.html"

#entrando na url
driver.get(url)
sleep(3)#esperando 3 segundos para a pagina carregar

lista_n_ordenada = driver.find_element_by_tag_name('ul')#Buscando 'ul'
lis = lista_n_ordenada.find_elements_by_tag_name('li')#Buscando 'li'
a1 = lis[0].find_element_by_tag_name('a').text #pegando o texto do a1
a2 = lis[1].find_element_by_tag_name('a').text #pegando o texto do a2

print(a1) #printando a1
print(a2) #printando a2

# ----------------------------------------------------#



# POR 'CLASS' ##

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_05_b.html"
#entrando na url
driver.get(url)

#encontrando os elemento por class
topico = driver.find_element_by_class_name('topico')
linguagens = driver.find_elements_by_class_name('linguagens')

#criando uma tupla pra mostrar os resultados
for linguagen in linguagens:
    print(
        (linguagen.find_element_by_tag_name('h2').text,
        linguagen.find_element_by_tag_name('p').text)
        )

driver.quit()

"""
Outros atributos globais:
    id
    class
    name \ especifico do input
    placeholder \ fica apagadinho dentro de um campo em um form
    autofocus
    acesskey
    title
    hidden
"""
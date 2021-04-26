#Eventos #
'''
    foco (focus/blur)
    mudança (charge)
'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_07_d.html"
#entrando na url
driver.get(url)

input_de_texto = driver.find_element_by_tag_name('input')
span = driver.find_element_by_tag_name('span')
p = driver.find_element_by_tag_name('p')

"""
Quando clicar no elemento 'input', então o texto 'Está com foco' deve ser o content de "span".

Quando clicar no elemento 'span', então o texto 'Está sem foco' deve ser o content de "span"
"""
input_de_texto.click()
assert 'está com foco' == span.text
span.click()
assert 'está sem foco' == span.text

"""
dado que o texto 'l' deve ser o content de 'p'
quando enviar algo no elemento 'input'
    o texto 'está com foco' deve ser o conteudo de 'span'
quando clicar em 'span'
    o texto 'está sem foco' deve ser o conteudo de 'span'
    o texto 'l' deve ser o content de 'p'
"""
assert p.text == '0', 'p não é zero'
input_de_texto.send_keys('batata')
assert 'está com foco' == span.text, 'está com foco não está em'
span.click()
assert 'está sem foco' == span.text, 'esta sem foco não está em'
assert p.text == '1', 'p não é um'


driver.quit()
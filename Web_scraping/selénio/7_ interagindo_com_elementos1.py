# SELETORES CSS
"""
 TIPOS DE SELETORES
    Básicos:
        -id             ('#id')         element
        -tipo ou tag    ('tag')         elements
        -classe         ('.class)       element / elements
        -Atributo       #ATRIBUTOS
        -universal      (*)             pega tudo da pagina
        -combinado      (tag[atributo])
    Seletores de grupo
        por lista       ( , )
    Combinados          #COMBINADOS
"""
# ATRIBUTOS
"""
[ATRIBUTO]
    .find_elements_by_css_selector('[atributo]')
[ATRIBUTO OPERADOR VALOR]
    [atributo=valor]    deve ser exatamente igual       
    [atributo*=valor]   deve correr em
    [atributo|=valor]   deve ser exatamente ou iniciar
    [atributo^=valor]   iniciado em
    [atributo$=valor]   terminado em
    [atributo~=valor]   um deve ser exatamente igual
"""
from selenium import webdriver
from time import sleep

b = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_06_a.html"
#entrando na url
b.get(url)
sleep(3)

#usando o atributo type [attr=valor]
'''
nome = b.find_element_by_css_selector('[type="text"]')
senha = b.find_element_by_css_selector('[type="password"]')
'''

#usando o atributo name [attr=valor]
'''
nome = b.find_element_by_css_selector('[name="nome"]')
senha = b.find_element_by_css_selector('[name="senha"]')
'''

#usando o atributo [attr*=valor]
'''
nome = b.find_element_by_css_selector("[name*='ome']")
senha = b.find_element_by_css_selector("[name*='nha']")
'''

#usando o atributo [attr|=valor]
'''
nome = b.find_element_by_css_selector("[name|='nome']")
senha = b.find_element_by_css_selector("[name|='senha']")
'''

#usando o atributo [attr^=valor]
'''
nome = b.find_element_by_css_selector("[name^='n']")
senha = b.find_element_by_css_selector("[name^='s']")
'''

#usando o atributo [attr$=valor]
'''
nome = b.find_element_by_css_selector("[name$='e']")
senha = b.find_element_by_css_selector("[name$='a']")
'''
'''
nome.send_keys('neto')
senha.send_keys('123')
'''

#COMBINADOS
'''
    IRMÃOS ADJACENTES   (A + B)     apartir de um elemento, busca outro aninhado com ele
    GERAL DE IRMÃOS     (A ~ B)     apartir de um elemento, busca todos os outros
    FILHOS              (A > B)     apartir de um elemento, pega tudo que tem aninhado denhtro dele
    DESCENDENTES        (A   B)     apartir de um elemento, pega tudo que esteja aninhado dentro ou fora dele
'''
#pegando todos os br's aninhados com div
b.find_elements_by_css_selector('div.form-group + br')

#pegando o br aninhados em div
b.find_elements_by_css_selector('div.form-group > br')

#pegando os form aninhados em body
b.find_elements_by_css_selector('body + form')

#pegando todos os br's aninhados com h2
b.find_elements_by_css_selector('h2 ~ br')

#pegando todos os br's aninhados em body
b.find_elements_by_css_selector('body br')

## para se divertir e aprender: https://flukeout.github.io
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://curso-python-selenium.netlify.app/aula_03.html"

#entrando na url
driver.get(url)

sleep(3)#esperando 3 segundos para a pagina carregar

#localizando os elementos pela tag
a = driver.find_element_by_tag_name('a')
p = driver.find_element_by_tag_name('p')
#Mostrando o texto das tags
print(f'texto de a: {a.text}')
print(f'texto de p: {p.text}')

#Fazendo um loop para clicar no link, gerar novos numeros, e pegar os numeros:
for click in range(10):
    ps = driver.find_elements_by_tag_name('p') #pegando mais de um elemento em P (volta uma lista)
    a.click() #clicando em a para gerar mais ps
    print(f'Valor do ultimo p: {ps[-1].text} Valor do click: {click}')
    print(f'Os valores são iguais? {ps[-1].text == str(click)}')

#fechando o navegador
driver.quit()
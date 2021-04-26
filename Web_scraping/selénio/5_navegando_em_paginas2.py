from selenium import webdriver
from time import sleep
from urllib.parse import urlparse

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://selenium.dunossauro.live/aula_04_b.html"
#entrando na url
driver.get(url)

url_parseada = urlparse(driver.current_url)
print(url_parseada) #mostra as partes da url
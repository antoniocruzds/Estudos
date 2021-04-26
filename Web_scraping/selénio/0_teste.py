#Abrindo o Chrome via python

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

url = "http://www.google.com.br"
driver.get(url)

                                                 ### WEB SCRAPING / RVEST ###

  #O Rvest é um pacote para estruturar arquivos HTML ou XML de forma eficiente, %>% 
  #tornando possível a obtenção de tags e seus atributos dentro de um arquivo. %>% 
  #Realiza requisições web para obtenção das páginas de interesse, buscando reduzir ao máximo a complexidade da programação. 

#PRONCIPAIS FUNÇÕES DO RVEST:

library(rvest) #Ativação do pacote

  #Para acessar páginas da web:
  
html_session() #abre uma sessão do usuário (baixa página, carrega cookies etc).
follow_link() jump_to() #acessa uma página web a partir de um link (tag <a>) ou url.
html_form() #carrega todos os formulários contidos numa página.
set_value() #atribui valores a parâmetros do formulário.
submit_form() #submete um formulário obtido em html_form.

  #Para trabalhar com arquivos HTML:
  
read_html() #lê o arquivo HTML de forma estruturada e facilita impressão.
html_nodes() #cria uma lista com os nós identificados por uma busca em CSS path ou XPath.
html_node() #é um caso especial que assume que só será encontrado um resultado.
html_text() #extrai todo o conteúdo de um objeto e retorna um texto.
html_table() #extrai o conteúdo de uma <table> e transforma em um data_frame.
html_attr() #extrai um atributo de uma tag, por exemplo href da tag <a>.

#fonte: <http://material.curso-r.com/scrape/> e <https://rvest.tidyverse.org/index.html>



### HTML; CSS; XML ###

    **HTML** #Linguagem de arcação para a construção de paginas web
#é uma lingagem de marcação. Utilizada para formatar textos e informações. %>% 
#estrutura dividida em head e body
#Apresentação de dados;
  
    **CSS** #Linguagem para deixar a informação mais "bonitinha"
#é uma linguagem utilizada para definir a aparencia de documentos(como XML, HTML e XHTML e etc..).
#O CSS define como serão exibidos os elementos contidos no código de um documento
#efetuar a separação entre o formato e o conteúdo de um documento;
  
    **XML** #Linguagem de marcação para a codificação de documentos
#Tecnologia para criar linguagem de marcação que descrevem dados de todos os tipos de uma forma estuturada
#Define elementos de marcação e gera uma linguagem personalizada
#Estrutura dividida em: prolog (declaração dos metadados adm, como a declaração do tipo de documento), e body (estutural e contexto)
#linguagem especifica para dados;
  


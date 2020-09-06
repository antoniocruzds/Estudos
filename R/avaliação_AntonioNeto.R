                           ## AVALIAÇÃO DE R ##

#QUESTÃO 1
    #Pasta criada na area de trabalho (ok)

#QUESTÃO 2
    #Salvar o arquivo baixado na pasta criada (ok)

#QUESTÃO 3
getwd() #verificando onde era o diretorio
setwd("C:\\Users\\anton\\OneDrive\\Área de Trabalho\\Avaliação_AntonioNeto") #setando o novo diretorio
getwd()#Verificando o local definido

#QUESTÃO 4
library(tidyverse) #Ativando o pacote tidyverse

#QUESTÃO 5
df <- read.csv2("aprovados_sisu_pas.csv", encoding = "UTF-8") #Criando um data.freme chamado "df" para receber a base de dados
View(df) #visualizando o dataframe

#QUESTAO 5.1
#BASE DOS ESTUDANTES DE MEDICINA
df_med_aprov_2017_AC <- df %>% #Sub-base 1
  filter(Curso == "Medicina (Bacharelado") %>% 
  filter(Semestre.de.aprovação == "2017/1") %>% 
  filter(Vaga == "Ampla Concorrência") %>% 
  filter(Status.de.aprovação == "APROVADO")

#QUESTÃO 5.2
#BASE DOS ESTUDANTES DE AGRONOMIA
df_agro_aprov_2017_AC <- df %>% #sub-base 2 ###ta com .2017 pois na prova esta assim, só mudei o agro
  filter(Curso == "Agronomia (Bacharelado") %>% 
  filter(Semestre.de.aprovação == "2018/1") %>% 
  filter(Vaga == "Ampla Concorrência") %>% 
  filter(Status.de.aprovação == "APROVADO")

#QUESTÃO 5.3
#CONTANDO OS ESTUDANTES DE MEDICINA EM 2017 POR TIPO DE VAGA
df_med_aprov_2017 <- df %>% 
  filter(Curso == "Medicina (Bacharelado") %>% 
  filter(Semestre.de.aprovação == "2017/1") %>% 
  filter(Status.de.aprovação == "APROVADO") %>% 
  count(Vaga)

#QUESTÃO 5.4
#CONTANDO OS ESTUDANTES DE AGRONOMIA EM 2017 POR TIPO DE VAGA
df_agro_aprov_2017 <- df %>% 
  filter(Curso == "Agronomia (Bacharelado") %>% 
  filter(Semestre.de.aprovação == "2017/1") %>% 
  filter(Status.de.aprovação == "APROVADO") %>% 
  count(Vaga)

rm(df_med_agro_2017)#Removendo sub-base que tinha errado

#QUESTÃO 5.5
#TABELA COM A QUANTIDADE DE ESTUDANTES APROVADOS POR CURSO
dt_tabela_aprov_2018_curso_vaga <- df %>% 
  filter(Semestre.de.aprovação == "2018/1") %>% 
  filter(Status.de.aprovação == "APROVADO") %>% 
  group_by(Curso) %>% 
  count(Vaga)

save

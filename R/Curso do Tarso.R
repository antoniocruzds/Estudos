library(tidyverse) #Ativando o pacote

%>% #Operador PIPE (ctrl, shift, m)
  
#OPERAÇÃO PARA ACHAR O MODULO DO COSSENO DE Y SEM O PIPE
x <- pi #pi= valor real de pi
y_ <- cos(x) #cos= cosseno de b
z <- abs(y_) #abs= modulo de y_

#OPERAÇÃO PARA ACHAR O MODULO COM O PIPE
b <- pi
y <- b %>% cos() %>% abs()

#CRIANDO UM NOVO DIRETORIO
setwd("C:\\Users\\anton\\OneDrive\\Área de Trabalho\\UFBA\\Ferramentas digitais\\R\\R aula (11-10)") #lembrar das barras duplas
getwd()#saber onde é o diretorio
save

bus <- read_csv("buz_copia.csv") #criando um objeto para receber a base de dados baixada
View(bus) #Visualisando o banco de dados do objeto

# FUNÇÃO FILTER
bus_filtro <- bus %>% filter(PROAE == "S") # SAIDA <- ENTRADA %>%  OPERAÇÃO // (data frame) filtra os alunos que recebem o beneficio (PROAE == "S")
View(bus_filtro) #Visualizar o filtro(data frame) com alunos que recebem
bus_filtro_reitoria <- bus %>% filter(ORIGEM1 == "Reitoria") #filtro para alunos que saem da reitoria 
View(bus_filtro_reitoria) #visualizar o filto dos alunos que saem da reitoria

#SELECT (Selecionador de variaveis)
bus_tabela <- bus %>%  #variavel bus_tabela com os dados do data bus
  filter(PROAE == "S") %>% #filtrar quem recebe o beneficio da proae
  select(SEXO, RENDA) %>%  #colocando/selecionando somente as variaveis renda e sexo
  table() #criar essa tabela

bus_tabela #abrir

#CRIANDO UM DATAFRAME COM IDADE, SEXO,RENDA
bus_isr <- bus %>% 
  select(IDADE, SEXO, RENDA) 

#COUNT ()
bus_tabela2 <-  bus %>% 
  filter(PROAE =="S") %>% #escolhemos só os aluno PROAE
  select(SEXO,RENDA) %>%  #Selecionando as variaveis
  count(RENDA, SEXO, sort = TRUE) #contando, sort = prioridade (true=quem tem mais)

#GRUP_BY
bus_viol_imp <- bus %>% 
  group_by(SEXO) %>% 
  count(I_VIOL) %>% 
  #ungroup() %>% 
  #select(I_VIOL, n) remove uma variavel que foi agrupada(as duas linhas)

#MUTATE
bus_mutate <- bus %>% 
  group_by(SEXO, I_VIOL) %>% 
  mutate(prop = n()/nrow(.)) %>% 
  select(SEXO, I_VIOL, prop)
  
#SUMMARISE (Esta função é responsável por resumir um banco de dados seguindo uma medida)
bus_prop <- bus %>% 
  group_by(SEXO, I_VIOL) %>% 
  summarise(prop = n()/ nrow(.))
save
0
#APRESENTAÇÃO DE TARSSO (https://tarssioesa.github.io/intro/#30)

save

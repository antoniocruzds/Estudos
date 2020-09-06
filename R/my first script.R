                                                      ### PRIMEIRO SCRIPT  11/10 ###

#Comando para saber meu diretorio de trabalho (WD)
getwd()

#Comando para escolher o meu diretorio de trabalho (wd)
setwd("C:\\Users\\anton\\OneDrive\\?rea de Trabalho\\UFBA\\Ferramentas digitais\\R") #Lembrar de colocar barra dupla
getwd()
save

#Comando para criar variaveis (usar o Alt-)
a <- 1 #objeto numerioco
b <- TRUE #objeto logical
c <- ("neto") #objeto charectere
d <- 50L #objeto Integer
e <- 5+8i #objeto comlex

#pra saber qual o tipo de variavel
class(a) 
class(b)
class(c)
class(d)
class(e)

#saber as variaveis existentes
ls()

#remover cada variavel
rm(aluno)
rm(t)
rm(w)
rm(x)
rm(y)

#remover todas as variaveis
rm(list=ls())

#criando vetores (reunir objetos do mesmo tipo)
idade <- c(22,18,25,15)
nomes <- c("neto","bea","marcos","leo")
estado.civil <- c(T,F,F,F)

#Data frame (reuniao de vetores), base de dados
df <- data.frame(idade, nomes, estado.civil)
df$idade #chamando determinado vetor
df[2,3]#chamando determinada lacuna

#instalando pactotes
install.packages("XML") #pacote para ler dados na internet
install.packages("tidyverse") #arquivo que trabalha com a manupula??o de dados

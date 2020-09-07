                                   #UTILIZANDO MÓDULOS

#Utilizamos o comando 'import' para adicionar modulos no python
#   Ex: import bebidas (importará todas as bebidas) {GENERALISTA}

#Podemos importar coisas especificas dentro de um modulo sem precisar importa-lo todo
#  Ex: from bebidas import agua (ele importará somente a água) {ESPECIFICO}

#Para saber quais bibliotecas estão disponiveis para instalação basta acessar python.org
#################################################################################

#Importando só a função que eu quero
from math import sqrt
num1 = int(input('Digite um numero: '))
raiz1 = sqrt(num1)
print('A raiz do número {}, é {:.2f}'.format(num1, raiz1))

#Importando todas as funções
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz do número {}, é {:.2f}'.format(num, math.ceil(raiz))) #pedindo pra arredondar pra cima

#################################################################################
#                                  Números aleatorios
import random
ran = random.random() #numeros entre 0 e 1
ran1 = random.randint(1, 100) #numero inteiro entre 1 e 100
print('número entre 0 e 1:', ran, ';Número entre 1 e 100:', ran1)

##################################################################################
#Exercicio 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
re = float(input('Digite um número real: '))
print('O número digitado foi {} e sua porção inteira é {}.'.format(re, (math.trunc(re))))

########################################################################################
#Exercício 017:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Qual o valor do Cateto oposto? '))
ca = float(input('Qual o valor do Cateto adjacente? '))
hin = (co ** 2 + ca ** 2) ** (1/2) #Normal
him = math.hypot(co, ca) #com a biblioteca math
print('o Valor da hipotenusa é {}'.format(hin))

################################################################################################
#Exercicio 018:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite um ângulo qualquer: '))
sen = math.sin((math.radians(ang)))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo inserido é {:.2f}, seu seno é {:.2f}, seu cosseno {:.2f}, e sua tangente é {:.2f}.'.format(ang, sen, cos, tang))

##############################################################################################
#Exercicio 019
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
n1 = str(input('Qual o nome do 1º aluno? '))
n2 = str(input('Qual o nome do 2º aluno? '))
n3 = str(input('Qual o nome do 3º aluno? '))
n4 = str(input('Qual o nome do 4º aluno? '))
lista1 = [n1, n2, n3, n4]
escolhido = random.choice(lista1)
print('O Aluno sorteado foi {}.'.format(escolhido))

#############################################################################################

#Exercicios 020
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
no1 = str(input('Qual o nome do 1º aluno? '))
no2 = str(input('Qual o nome do 2º aluno? '))
no3 = str(input('Qual o nome do 3º aluno? '))
no4 = str(input('Qual o nome do 4º aluno? '))
lista2 = [no1, no2, no3, no4]
ordem = random.shuffle(lista2) #Embaralha
print('A ordem de apresentação é: ')
print(lista2)

######################################################################################
#Exercicio 021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex012.mp3')
pygame.mixer.music.play()
pygame.event.wait()

############################################################################################

                    #OPERADORES ARITIMETICOS#

# o == significa igualdade, o = significa atribuição

# + adição              (5 + 2 == 7)
# - Subtração           (5 - 2 == 3)
# * Multiplicação       (5 * 2 == 10)
# / Divisão             (5 / 2 == 2.5)
# ** Potencia           (5 ** 2 == 25)
# // Divisão inteira    (5 // 2 == 2)   dividir sem usar virgula
# % Resto da divisão    (5 % 2 == 1)    o que sobra da divisão

    #ORDEM DE PRECEDENCIA#
# 1 -> ();
# 2 -> **;
# 3 -> * , /, //, %;
# 4 -> + , -;

#ex:
# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * ( 5 + 4 ) ** 2 == 243
# 81 ** (1/2) == 9

                    #FORMATAÇÃO E DICAS DO PRINT
print('oi' * 5) #multiplica as palavras
print('='*20)

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}'.format(nome))       #o nome aparece em 20 caracteres
print('Prazer em te conhecer {:>20}'.format(nome))      #nome alinhado a esquerda em 20 espaços
print('Prazer em te conhecer {:<20}'.format(nome))      #nome alinhado a direita em 20 espaços
print('Prazer em te conhecer {:^20}'.format(nome))      #nome centralizado em 20 espaços
print('Prazer em te conhecer {:=^20}'.format(nome))    #nome centralizado com = em volta

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {},\nO produto é {},\nA divisão {:.3f}'.format(s, m, d), end=' ')  #o end='' == juntar as linhas  // O \n == quebrar a linha
print(', a divisão inteira {}, \nA potencia {:.3f}' .format(di, e))                #o {:.3} serve pra delimitar a quantidade de casas apos o ponto

#EXERCICIO 005
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))
print(' O número é {}, seu antecessor é {}, e seu sucessor é {}'.format(n, (n - 1), (n + 1)))

#EXERCICIO 006
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

a = int(input('Digite um número inteiro: '))
print(' O número é {}, seu dobro {}, seu triplo é {}, e sua raiz quadrada é {}'.format(n, (a * 2), (a* 3), (a **(1/2))))

#EXERCICIO 007
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a egunda nota: '))
print('a média do aluno é {}'.format((n1 + n2)/2))

#EXERCICIO 008
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

mt = float(input('Digite um valor em métros: '))
print('O Valor em metros é {}, em centímetros é {:.0f}, e em milímetros é {:.0f}'.format(mt, (mt*100), (mt*1000)))

#EXERCICIO 009
#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

t = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(t, 1, t*1))
print('{} x {:2} = {}'.format(t, 2, t*2))
print('{} x {:2} = {}'.format(t, 3, t*3))
print('{} x {:2} = {}'.format(t, 4, t*4))
print('{} x {:2} = {}'.format(t, 5, t*5))
print('{} x {:2} = {}'.format(t, 6, t*6))
print('{} x {:2} = {}'.format(t, 7, t*7))
print('{} x {:2} = {}'.format(t, 8, t*8))
print('{} x {:2} = {}'.format(t, 9, t*9))
print('{} x {:2} = {}'.format(t, 10, t*10))
print('-' * 12)

#EXERCICIO 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considerando o dolar = 3.27

din = float(input('Quantos reais você tem? R$'))
print('Com R$ {}, você pode comprar {:.2f} Dolares'.format(din, (din / 3.27)))

#EXERCICIO 011
#Faça um programa que leia a largura e a altura de uma parede em metros,
    #calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
print('Sua parede tem {}m², e pra pintar ela você precisará de {} litros de tinta.'.format(l * h, (l * h)/2))

#EXERCICIO 012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pre = float(input('Qual o valor do produto? R$'))
des = (pre * 5)/100
print('O produto custa R${:.2f}, mas com o desconto de 5% custará R${:.2f}'.format(pre, (pre - des)))

#EXERCICIO 013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o salario atual do funcionario? R$'))
reaj = (sal * 15)/100
print('O Salário do funcionario era R${}, mas com o reajuste de 15% passou a ser R${}'.format(sal, (sal + reaj)))

#EXERCICIO 014
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Qual a temperatura em C°? '))
f = ((9 * temp) / 5) + 32
print('A temperatura em C° é {}, e em F° é {}'.format(temp, f))

#EXERCICIO 015
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
     # e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Você alugou o carro por quantos dias? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é de R${}'.format((60 * dias) + (0.15 * km)))
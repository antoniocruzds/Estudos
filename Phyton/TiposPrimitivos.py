            ### TIPOS DE DADOS EXISTENTES ###
                        # MODULO 2 #

# int -> Números inteiros ( 45 / 5 / 1458)
# float -> Números com ponto flutuante ( 0.5 / 7.0)
# bool -> Valores verdadeiros ou falsos (True / False)
# str -> strings ou palavras entre aspas ('Olá' / '7.5' / '')

#o 'type' é usado para saber qual o tipo do objeto

            #MODOS DE USAR O PRINT
x = 1 + 2
print(type(x)) #pra saber o tipo do objeto
print('A soma vale', x) #modo normal
print('A soma vale {} '.format(x)) #atribui o que tem no .format às chaves/mascaras

            #FAZENDO USO DOS TIPOS DE VARIAVEIS E PRINT

A = int(input('Digite um número: ')) #informando o tipo
print(type(A))
B = int(input('Digite outro número: ')) #informando o tipo
print(type(B))
C = input('Digite um valor qualquer: ') #sem informar o tipo
print(type(C))
S = A + B
print('A soma entre A e B é igual a', S) #usando um tipo de print
print('A soma entre {} e {} é igual a {}!' .format(A,B,S)) #usando print com .format


#EXERCICIO 003
#Fazer um rpograma que leia dois números e mostre a soma entre eles:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a {}!' .format(n1,n2,soma))

#EXERCICIO 004
#FAZER UM RPOGRAMA QUE LEIA O QUE FOI DIGITADO E DIGA O SEU TIPO E O QUE ELE NÃO É:

k = input('Digite algo: ')
print('O tipo primitivo disso é: ', type(k))
print('Só tem espaços? ', k.isspace())
print('É um número? ', k.isnumeric())
print('É alfabetico? ', k.isalpha())
print('É alfanumerico ?', k.isalnum())
print('Está em maiusculas?', k.isupper())
print('Esté em minusculas? ', k.islower())
print('Está capitalizada? ', k.istitle())

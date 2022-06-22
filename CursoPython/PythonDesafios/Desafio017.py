#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
co = int(input('Qual o valor do cateto oposto? '))
ca = int(input('Qual o valor do cateto adjacente? '))
h = math.sqrt(co ** 2 + ca ** 2)
print('A hipotenusa dos catetos deste triângulo retângulo tem o comprimento {}'.format(int(h)))

#RESOLUÇÃO PROFESSOR:
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2}'.format(hi))
#OU
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2}'.format(hi))

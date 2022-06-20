#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
co = int(input('Qual o valor do cateto oposto? '))
ca = int(input('Qual o valor do cateto adjacente? '))
h = sqrt(co ** 2 + ca ** 2)
print('A hipotenusa dos catetos deste triângulo retângulo tem o comprimento {}'.format(int(h)))

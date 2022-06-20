#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = int(input('Escreva um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Do ângulo {}º, temos o seno {}, cosseno {} e tangente {}.'.format(a, s, c, t))

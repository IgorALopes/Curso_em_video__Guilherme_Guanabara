#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
a = float(input('Escreva um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Do ângulo {}º, temos o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(a, s, c, t))

#RESOLUÇÃO PROFESSOR:
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
coseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, coseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

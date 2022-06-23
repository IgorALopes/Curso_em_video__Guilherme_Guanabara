#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o valor do comprimento de uma reta: '))
b = float(input('Digite outro valor do comprimento de uma reta: '))
c = float(input('Digite outro valor do comprimento de uma reta: '))
if (a + b) > c and (b + c) > a and (a + c) > b:
    print('Essas retas podem formar um TRIÂNGULO!')
else:
    print('Essas retas NÃO podem formar um TRIÂNGULO')

#RESOLUÇÃO PROFESSOR:
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

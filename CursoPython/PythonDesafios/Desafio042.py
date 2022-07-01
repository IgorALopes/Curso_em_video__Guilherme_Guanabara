# Reforça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais; Isósceles: dois lados iguais; Escaleno: todos os lados diferentes.
a = float(input('Digite o valor do comprimento de uma reta: '))
b = float(input('Digite outro valor do comprimento de uma reta: '))
c = float(input('Digite outro valor do comprimento de uma reta: '))
if (a + b) > c and (b + c) > a and (a + c) > b:
    if a == b and b == c and c == a:
        print('Essas retas podem formar um TRIÂNGULO EQUILÁTERO!')
    elif a == b or b == c or c == a:
        print('Essas retas podem formar um TRIÂNGULO ISÓSCELES!')
    elif a != b and b != c and c != a:
        print('Essas retas podem formar um TRIÂNGULO ESCALENO!')
else:
    print('Essas retas NÃO podem formar um TRIÂNGULO')

# RESOLUÇÃO PROFESSOR:
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo !', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

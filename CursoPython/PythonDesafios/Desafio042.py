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

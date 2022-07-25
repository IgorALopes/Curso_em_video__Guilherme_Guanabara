# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = c = 0
while True:
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        print('PROGRAMA ENCERRADO!')
        break
    for c in range(1, 11):
        mult = n * c
        print(f'{n} x {c} = {mult}')
        c += 1

# RESOLUÇÃO PROFESSOR:
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRAD. Volte sempre!')

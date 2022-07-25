# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
t1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razão desta PA: '))
c = 0
while c < 10:
    pa = t1 + r * c
    c += 1
    print('{} '.format(pa), end='➡ ')
print('ACABOU')

# RESOLUÇÃO PROFESSOR:
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Priemiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➡ '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')

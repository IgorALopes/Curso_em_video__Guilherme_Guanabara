# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.
t1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razão desta PA: '))

u = t1 + (10 - 1) * r
u = u + 1

for c in range(t1, u, r):
    print(c)

# RESOLUÇÃO PROFESSOR:
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='➡ ')
print('ACABOU')

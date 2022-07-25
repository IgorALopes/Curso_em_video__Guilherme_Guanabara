# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
t1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razão desta PA: '))
c = 0
termos = 10
pa2 = 0
t2 = 1
while c < termos:
    pa = t1 + r * c
    c += 1
    pa2 = pa + r
    print('{}'.format(pa), end=' ➡ ')
print('PAUSA')
while t2 > 0:
    t2 = int(input('Quantos termos você quer mostrar a mais? '))
    if t2 == 0:
        print('Progressão finalizada com {} termos mostrados.'.format(termos))
    else:
        termos += t2
        c2 = 0
        pa3 = 0
        while c < termos:
            pa3 = pa2 + r * c2
            c += 1
            pa2 = pa3 + r
            print('{}'.format(pa3), end=' ➡ ')
        print('PAUSA')

# RESOLUÇÃO PROFESSOR:
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Priemiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➡ '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

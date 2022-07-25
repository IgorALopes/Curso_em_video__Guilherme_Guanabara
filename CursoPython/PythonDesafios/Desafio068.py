# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('JOGO DE PAR OU ÍMPAR')
cont = 0
while True:
    jog = int(input('Digite um valor: '))
    parimp = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    comp = randint(0, 11)
    soma = jog + comp
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {jog} e o computador {comp}. Total de {soma} que é {resultado}.')
    if parimp == 'P' and resultado == 'PAR':
        print(f'VOCÊ GANHOU!!')
        print(f'Jogue novamente...')
        cont += 1
    elif parimp == 'I' and resultado == 'ÍMPAR':
        print(f'VOCÊ GANHOU!!')
        print(f'Jogue novamente...')
        cont += 1
    else:
        print(f'PERDEU! Você ganhou {cont} vezes.')
        break

# RESOLUÇÃO PROFESSOR:
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

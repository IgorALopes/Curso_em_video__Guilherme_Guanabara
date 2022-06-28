# Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('-=-'*7)
print('VAMOS JOGAR JOKENPÔ!')
print('-=-'*7)
sleep(2)
print('Tente me vencer!')
sleep(1)
player = str(input('Escolha e escreva "PEDRA", "PAPEL" ou "TESOURA"!\n')).strip().upper()
if player != 'PEDRA' and player != 'PAPEL' and player != 'TESOURA':
    print('Por favor, escolha uma opção válida. Começe novamente!')
else:
    print('Certo! Agora eu vou escolher!')
    sleep(1.5)
    print('Hummm...')
    joklist = ['PEDRA', 'PAPEL', 'TESOURA']
    machine = random.choice(joklist)
    sleep(2)
    print('Já sei!')
    sleep(1)
    print('Vamos começar!')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)
    if player == machine:
        print('EMPATOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PEDRA' and machine == 'TESOURA':
        print('Aff. VOCÊ GANHOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PEDRA' and machine == 'PAPEL':
        print('Haha! GANHEI! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'TESOURA' and machine == 'PAPEL':
        print('Aff. VOCÊ GANHOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'TESOURA' and machine == 'PEDRA':
        print('Haha! GANHEI! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PAPEL' and machine == 'PEDRA':
        print('Aff. VOCÊ GANHOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PAPEL' and machine == 'TESOURA':
        print('Haha! GANHEI! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')

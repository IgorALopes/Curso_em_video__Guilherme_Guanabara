# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
c = 0
n = randint(0, 10)
pn = ''
print('Tente adivinhar o número que estou pensando!')
while n != pn:
    pn = int(input('Digite um número de 0 a 10: '))
    if pn != n:
        c += 1
        print('Você errou, tente novamente!')
    elif pn > 10:
        print('Digite um número válido.')
print('Você acertou!! Você tentou {} vezes até acertar.'.format(c))

# RESOLUÇÃO PROFESSOR:
# from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas! Parabéns!'.format(palpites))

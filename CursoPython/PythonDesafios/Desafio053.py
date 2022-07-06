# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
fr = str(input('Escreva algo e descubra se é um PALÍNDROMO: ')).strip().upper()
frsp = fr.split()
frjo = ''.join(frsp)
frinv = frjo[::-1]
if frjo == frinv:
    print('Isto É um Palíndromo!')
    print('Sua frase é {} e o inverso é {}'.format(frjo, frinv))
else:
    print('Isto NÃO é um Palíndromo!')
    print('Sua frase é {} e o inverso é {}'.format(frjo, frinv))

# RESOLUÇÃO PROFESSOR:
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# RESOLUÇÃO PROFESSOR - MÉTODO SEM O FOR:

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

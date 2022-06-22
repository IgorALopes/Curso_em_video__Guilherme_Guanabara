#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
f = str(input('Escreva uma frase que contenha pelo menos uma letra a: ')).strip().lower()

print('Nesta frase, a letra "a" aparece {} vezes.'.format(f.count('a')))
print('A primeira letra "a" aparece na posição {}.'.format(f.find('a')))
print('A última letra "a" aparece na posição {}.'.format(f.rfind('a')))

#RESOLUÇÃO PROFESSOR:
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
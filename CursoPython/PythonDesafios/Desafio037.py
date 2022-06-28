# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual seá a basa de conversão: 1 para binário, 2 para octal, 3 para hexadecimal.
n = int(input('Escreva um número: '))
option = int(input('Escolha uma opção de bases de conversão:\n1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\n'))
bina = format(n, "b")
octa = format(n, "o")
hexa = format(n, "x")
if option == 1:
    print('A forma BINÁRIA para o número {} é {}.'.format(n, bina))
elif option == 2:
    print('A forma OCTAL para o número {} é {}.'.format(n, octa))
elif option == 3:
    print('A forma HEXADECIMAL para o número {} é {}.'.format(n, hexa))
else:
    print('Opção inválida! Escolha entre as opções 1, 2 ou 3.')

# RESOLUÇÃO PROFESSOR:
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 1:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 1:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')

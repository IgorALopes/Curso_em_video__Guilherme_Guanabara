#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print('Alfanumérico?', a.isalnum())
print('Alfabético?', a.isalpha())
print('Numérico?', a.isnumeric())
print('Maiúsculo?', a.isupper())
print('Minúsculo?', a.islower())
print('Tudo são números decimais?', a.isdecimal())
print('Espaço em branco?', a.isspace())
print('Tudo são letras do alfabeto?', a.isascii())
print('Tudo são digitos?', a.isdigit())
print('É um identificador?', a.isidentifier()) #A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print('A string pode ser printada?', a.isprintable())
print('Cada palavra inicia com letras maiúsculas? É um título?', a.istitle())

#RESOLUÇÃO PROFESSOR:
a = input('Digite algo: ')
print('O tipo primitivo do valor {} é '.format(a), type(a))
print('{} Só tem espaços? '.format(a), a.isspace())
print('{} É um número? '.format(a), a.isnumeric())
print('{} É alfabético? '.format(a), a.isalpha())
print('{} É alfanumérico? '.format(a), a.isalnum())
print('{} Está em maiúsculas? '.format(a), a.isupper())
print('{} Está em minúsculas? '.format(a), a.islower())
print('{} Está capitalizada? '.format(a), a.istitle()) #Começa com letra maiúscula


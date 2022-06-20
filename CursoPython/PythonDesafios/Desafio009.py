#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número e veja a tabuada: '))
print('A tabuada do número {d} é: \n 1 x {d} = {t1} \n 2 x {d} = {t2} \n 3 x {d} = {t3} \n 4 x {d} = {t4} \n 5 x {d} = {t5} \n 6 x {d} = {t6} \n 7 x {d} = {t7} \n 8 x {d} = {t8} \n 9 x {d} = {t9} \n 10 x {d} = {t10}'.format(d=n, t1=n*1, t2=n*2, t3=n*3, t4=n*4, t5=n*5, t6=n*6, t7=n*7, t8=n*8, t9=n*9, t10=n*10))

#RESOLUÇÃO PROFESSOR:
num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 12)
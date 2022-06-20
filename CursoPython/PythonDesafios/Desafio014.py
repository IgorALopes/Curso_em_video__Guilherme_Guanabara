#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
c = float(input('Qual a temperatura em ºC? '))
f = c * 1.8 + 32
print("A temperatura {:.1f}ºC corresponde a {:.1f}ºF.".format(c, f))

#RESOLUÇÃO PROFESSOR:
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))

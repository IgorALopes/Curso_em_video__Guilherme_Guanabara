#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = int(input('Digite um valor em metros: '))
print('O valor {} digitado em metros, equivale a {} centímetros e {} milímetros.'.format(n, n*100, n*1000))

#RESOLUÇÃO PROFESSOR:
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm.'.format(medida, cm, mm))
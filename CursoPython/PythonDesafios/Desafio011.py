#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
pa = float(input('Qual a altura da parede em metros? '))
pl = float(input('Qual a largura da parede em metros? '))
pal = pa*pl
print('A área da parede é de {:.3f}m². Serão necessários {:.3f} litros de tinta para pintá-la.'.format(pal, pal/2))

#RESOLUÇÃO PROFESSOR:
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))


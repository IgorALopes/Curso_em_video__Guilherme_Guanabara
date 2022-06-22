#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
c = input('Qual a sua cidade? ')
print('Ela começa com o nome "SANTO"? {}'.format('santo' in c))

#RESOLUÇÃO PROFESSOR:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

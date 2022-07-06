# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
a1 = int(input('Em que ano a 1ª pessoa nasceu? '))
a2 = int(input('Em que ano a 2ª pessoa nasceu? '))
a3 = int(input('Em que ano a 3ª pessoa nasceu? '))
a4 = int(input('Em que ano a 4ª pessoa nasceu? '))
a5 = int(input('Em que ano a 5ª pessoa nasceu? '))
a6 = int(input('Em que ano a 6ª pessoa nasceu? '))
a7 = int(input('Em que ano a 7ª pessoa nasceu? '))
anoagora = date.today().year
idade = [anoagora - a1, anoagora - a2, anoagora - a3, anoagora - a4, anoagora - a5, anoagora - a6, anoagora - a7]
contmaior = 0
contmenor = 0
for c in range(0, len(idade)):
    if idade[c] >= 21:
        contmaior += 1
    else:
        contmenor += 1
print('Há {} maior(es) de idade e {} joven(s).'.format(contmaior, contmenor))

# RESOLUÇÃO PROFESSOR:
#from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo, tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))

# TREINO - Adicionei a idade ao Print.
#from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
list = []
for pess in range(0, 7):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess+1)))
    idade = atual - nasc
    list.append(idade)
    if idade >= 21:
        totmaior += 1
        print('A {}ª pessoa tem {} anos de idade.'.format(pess+1, list[pess]))
    else:
        totmenor += 1
        print('A {}ª pessoa tem {} anos de idade.'.format(pess+1, list[pess]))
print('Ao todo, tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))

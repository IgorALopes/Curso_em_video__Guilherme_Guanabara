#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM; Até 14 anos: INFANTIL; Até 19 anos: JUNIOR; Até 20 anos: SÊNIOR; Acima: MASTER.
from datetime import date
ano = int(input('Qual seu ano de nascimento: '))
anoagora = date.today().year
idade = anoagora - ano
if idade <= 9:
    print('Sua categoria de natação é MIRIM')
elif idade <= 14:
    print('Sua categoria de natação é INFANTIL')
elif idade <= 19:
    print('Sua categoria de natação é JUNIOR')
elif idade <= 20:
    print('Sua categoria de natação é SÊNIOR')
else:
    print('Sua categoria de natação é MASTER')
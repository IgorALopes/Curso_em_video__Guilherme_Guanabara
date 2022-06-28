#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Sele ainda vai se alista ao serviço militar.; Se é hora de se alistar; Se já passou o tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Qual seu ano de nascimento: '))
anoagora = date.today().year
if anoagora - ano > 18:
    print('Já passou o tempo de alistamento militar obrigatório em {} ano(s).'.format(anoagora - ano - 18))
elif anoagora - ano < 18:
    print('Falta(m) {} ano(s) para o seu alistamento militar obrigatório.'.format(18 - (anoagora - ano)))
else:
    print('Seu alistamento militar obrigatório ocorrerá este ano ({}).'.format(anoagora))

# RESOLUÇÃO PROFESSOR:
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))

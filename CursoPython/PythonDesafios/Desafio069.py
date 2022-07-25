# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maioridade = 0
sexomasc = 0
femvinte = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade == 19 and sexo == 'F':
        femvinte += 1
        maioridade += 1
    elif idade <= 18 and sexo == 'F':
        femvinte += 1
    elif idade > 18 and sexo == 'F':
        maioridade += 1
    elif idade > 18 and sexo == 'M':
        maioridade += 1
        sexomasc += 1
    elif idade <= 18 and sexo == 'M':
        sexomasc += 1
    maispess = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if maispess == 'N':
        break
print(f'Há {maioridade} pessoas maiores de 18 anos.')
print(f'Há {sexomasc} pessoas do sexo Masculino.')
print(f'Há {femvinte} mulheres com menos de 20 anos de idade.')

# RESOLUÇÃO PROFESSOR:
tot18 = toth = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos')

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
nomelist = []
idadelist = []
sexolist = []
ihmaior = 0
nmaior = ''
isexomenor = 0
for c in range(1, 5):
    print('Cadastro da Pessoa {}:'.format(c))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper().strip()
    nomelist.append(nome)
    idadelist.append(idade)
    sexolist.append(sexo)
    if c == 1 and sexo == 'M':
        ihmaior = idade
        nmaior = nome
    if idade > ihmaior and sexo == 'M':
        ihmaior = idade
        nmaior = nome
imed = sum(idadelist) / len(idadelist)
print('A média de idade deste grupo de pessoas é de {:.1f} anos.'.format(imed))
print('O homem com maior idade é {} e tem {} anos.'.format(nmaior, ihmaior))
for f in range(len(sexolist)): # Percebi um erro na interpretação do enunciado e tive que ajustar meu código, mas já havia visto a resolução. Estava utilizando listas como esta.
    if 'F' == sexolist[f] and idadelist[f] < 20:
        isexomenor += 1
print('Há {} mulhere(s) com menos de 20 anos de idade.'.format(isexomenor))

# RESOLUÇÃO PROFESSOR:
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O homem mais velho te {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = 'x'
while s == 'x':
    s = str(input('Digite o sexo (M/F): ')).strip().upper()
    if s == 'M':
        s = 'Masculino'
    elif s == 'F':
        s = 'Feminino'
    else:
        s = 'x'
        print('Digite uma opção válida.')
print('Você escolheu {}'.format(s))

# RESOLUÇÃO PROFESSOR:
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # [0] pega somente a primeira letra digitada.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

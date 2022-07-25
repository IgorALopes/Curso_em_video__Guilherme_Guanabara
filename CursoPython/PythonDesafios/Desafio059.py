# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar; [ 2 ] multiplicar; [ 3 ] maior; [ 4 ] novos números; [ 5 ] sair do programa; Seu programa deverá realizar a operação solicitada em cada caso.
loop_menu = True
loop_num = True
while loop_num == True:
    Numero1 = int(input('Escreva um número: '))
    Numero2 = int(input('Escreva outro número: '))
    loop_menu = True
    while loop_menu == True:
        menu = int(input('#=#' * 10 + '\nEscolha uma opção:\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n'))
        if menu == 1:
            print('A soma entre {} e {} é {}.'.format(Numero1, Numero2, Numero1 + Numero2))
        elif menu == 2:
            print('A multiplicação entre {} e {} é {}.'.format(Numero1, Numero2, Numero1 * Numero2))
        elif menu == 3:
            if Numero1 > Numero2:
                print('O maior número é {}'.format(Numero1))
            elif Numero2 > Numero1:
                print('O maior número é {}'.format(Numero2))
            else:
                print('Os valores são iguais.')
        elif menu == 4:
            loop_num = True
            loop_menu = False
        elif menu == 5:
            loop_menu = False
            loop_num = False
            print('Encerrando o programa. Obrigado.')
        else:
            print('Escolha uma opção inválida.')

# RESOLUÇÃO PROFESSOR:
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos número
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>>> Qual é a opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

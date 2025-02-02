opcoes = 1
while opcoes != 5:
    numero1 = int(input('Digite um valor:'))
    numero2 = int(input('Digite outro valor:'))
    opcoes = int(input('[1] SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA'))
    if opcoes == 1:
        soma = numero1 + numero2
        print('A soma entre {} e {} resultou em {}'.format(numero1,numero2,soma))
    elif opcoes == 2:
        multiplica = numero1 * numero2
        print('A multiplicação entre {} e {} resultou em {}'.format(numero1,numero2,multiplica))
    elif opcoes == 3:
        if numero1 > numero2:
            maior = numero1
            print('O {} é maior que {}'.format(numero1, numero2))
        else:
            maior = numero2
            print('O {} é maior que {}'.format(numero2, numero1))
    while opcoes == 4:
        numero1 = int(input('Digite um valor:'))
        numero2 = int(input('Digite outro valor:'))
        opcoes = int(input('[1] SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA'))
    if opcoes == 1:
     soma = numero1 + numero2
     print('A soma entre {} e {} resultou em {}'.format(numero1, numero2, soma))
    elif opcoes == 2:
     multiplica = numero1 * numero2
     print('A multiplicação entre {} e {} resultou em {}'.format(numero1, numero2, multiplica))
    elif opcoes == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
print('PROGRAMA ENCERRADO, ATÉ A PRÓXIMA!')




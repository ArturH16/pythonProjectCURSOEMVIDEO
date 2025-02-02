from random import choice
pessoa = int(input('Digite 1 para pedra, 2 para tesoura e 3 para papel:'))
lista = ['pedra', 'papel' , 'tesoura']
computador = choice(lista)
print('O computador escolheu {}'.format(computador))
if pessoa == 1 and computador == 'pedra':
    print('EMPATE')
elif pessoa == 1 and computador == 'papel':
    print('O COMPUTADOR GANHOU')
elif pessoa == 1 and computador == 'tesoura':
    print('VOCÊ GANHOU')
elif pessoa == 2 and computador == 'pedra':
    print('O COMPUTADOR GANHOU')
elif pessoa == 2 and computador == 'papel':
    print('VOCÊ GANHOU')
elif pessoa == 2 and computador == 'tesoura':
    print('EMPATE')
elif pessoa == 3 and computador == 'pedra':
    print('VOCÊ GANHOU')
elif pessoa == 3 and computador == 'papel':
    print('EMPATE')
elif pessoa == 3 and computador == 'tesoura':
    print('O COMPUTADOR GANHOU')
else:
    print('INVÁLIDO. SELECIONE PEDRA,PAPEL OU TESOURA')
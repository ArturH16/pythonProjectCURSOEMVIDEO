from random import randint
computador = randint(0,5)
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('Parabéns, você adivinhou!')
else:
    print('GANHEI! Eu pensei no número {}'.format(computador))



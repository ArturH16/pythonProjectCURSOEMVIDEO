from random import randint
computador = randint(0,10)
tentativas = 0
jogador = int(input('O computador pensará em um número de 0 a 10, e você deve tentar adivinhar o que ele pensar:'))
while jogador != computador:
    jogador = int(input('O computador pensará em um número de 0 a 10, e você deve tentar adivinhar o que ele pensar:'))
    tentativas += 1
print('ADIVINHOU! Você fez {} palpites até adivinhar'.format(tentativas))

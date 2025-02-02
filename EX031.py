p = int(input('Digite a distância da sua viagem:'))
if p <= 200:
    x = p * 0.5
    print('O preço da sua viagem é de {} reais'.format(x))
else:
    a = p * 0,45
    print('O preço da sua viagem é de {} reais'.format(a))

p = int(input('Qual a velocidade atual do carro em km/h?'))
if p <= 80:
    print('Você está dentro do limite permitido. Tenha um bom dia!')
else:
    x = p - 80
    multa = 7 * x
    print('MULTADO! Você excedeu o limite permitido de 80 km/h \n Você deve pagar uma multa de {} reais'.format(multa))
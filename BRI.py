from math import sqrt,pi
question = float(input('Qual a circunferência da sua cintura em centímetros?'))
questiontwo = float(input('Qual a sua altura em centímetros?'))
try:
    formula = 364.2 - 365.5 * sqrt(1 - ((question / (2 * pi))**2) / (0.5 * questiontwo))
    print('Seu BRI é de {}'.format(formula))
except ValueError:
    print("Os valores inseridos resultam em uma operação inválida na raiz quadrada.")

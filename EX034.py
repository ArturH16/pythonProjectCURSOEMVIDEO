salario = int(input('Qual o salário do funcionário em reais?:'))
if salario > 1250:
    a = salario * 1.10
    print('O novo valor do salário é de {} reais'.format(a))
else:
    a = salario * 1.15
    print('O novo salário é de {} reais'.format(a))
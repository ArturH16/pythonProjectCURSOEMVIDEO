emprestimo = int(input('Qual o valor da casa?'))
salario = int(input('Qual o salário do comprador?'))
tempo = int(input('Em quantos anos vai ser pago?'))
prestacao = emprestimo / tempo
if prestacao > 0.3 * salario:
    print('O empréstimo foi negado!')
else:
    print('O empréstimo foi aprovado!')
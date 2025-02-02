soma = 0
for c in range(1,7):
    num = int(input('DIGITE UM NÚMERO INTEIRO:'))
    if num % 2 == 0:
     soma += num
print('A soma entre os valores inteiros pares é de: {}'.format(soma))
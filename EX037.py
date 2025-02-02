numero = int(input('Digite um valor inteiro:'))
conversao = int(input('Escolha 1 para binário, 2 para octal e 3 para hexadecimal:'))
if conversao == 1:
    print('O {} convertido em binário é: {}'.format(numero,bin(numero)[2:]))
elif conversao == 2:
    print('O {} convertido em octal é: {}'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('O {} convertido em hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Inválido. Por favor, tente novamente')
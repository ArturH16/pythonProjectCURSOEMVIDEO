n = int(input('Digite um valor:'))
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
n3 = int(input('Digite um valor:'))
tupla = n,n1,n2,n3
if n1 or n2 or n3 or n % 2 == 0:
    print('Os valores pares foram :',end=' ')
if n % 2 == 0:
    print(n,end='  ')
if n1 % 2 == 0:
    print(n1,end='  ')
if n2 % 2 == 0:
    print(n2,end='  ')
if n3 % 2 == 0:
    print(n3,end='  ')
if n % 2 != 0 and n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
    print('Não houve valor par')
if n or n1 or n2 or n3 == 9:
    print(f'\nO nove apareceu {tupla.count(9)} vezes')
else:
    print('O nove não apareceu nenhuma vez')
if n == 3 or n1 == 3 or n2 == 3 or n3 == 3:
    print(f'O 3 apareceu pela primeira vez na {tupla.index(3)} posição')
else:
    print('O 3 não apareceu nenhuma vez')



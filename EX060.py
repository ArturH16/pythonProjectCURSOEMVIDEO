from math import factorial
fatorial = int(input('Digite um número e descubra seu fatorial:'))
c = fatorial
print('Calculando {}!'.format(fatorial))
while c > 0:
    print('{}'.format(c),end ='')
    print(' x ' if c > 1 else ' = ',end = '')
    c-= 1
print('{}'.format(factorial(fatorial)))

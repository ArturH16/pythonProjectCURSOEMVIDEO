num= int(input('Digite um valor de 0 a 9999'))
n = num % 10
a = num // 10 % 10
b = num // 100 % 10
c = num  // 1000 % 10
print('Milhar: {}'.format(c))
print('Centena: {}'.format(b))
print('Dezena: {}'.format(a))
print('Unidade: {}'.format(n))



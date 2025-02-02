from unicodedata import decimal

p = int(input('Direi se o número digitado é impar ou par:'))
x = p % 2
if x == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')
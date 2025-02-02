from math import sqrt
coposto= float(input('Digite o valor do cateto oposto'))
cadjacente= float(input('Digite o valor do cateto adjacente'))

h= coposto**2 + cadjacente**2
print('\33[1;30;41m A hipotenusa vai medir {:.2f}\33[m'.format(sqrt(h)))




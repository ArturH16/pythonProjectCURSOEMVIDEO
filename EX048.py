s = 0
count = 0
for c in range (1, 501 , +2):
    if c % 3 == 0:
        count += 1
        s = s + c
print('A soma de todos os {} números multiplos de 3 e impares de 1 a 500 é {}'.format(count,s))

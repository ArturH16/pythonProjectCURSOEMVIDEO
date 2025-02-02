from random import randrange
tupla = tupla1 = tupla2 = tupla3 = tupla4 =rand = menor = maior = 0
while True:
    rand = randrange(0, 1000)
    tupla += rand
    maior = tupla
    menor = tupla
    rand = randrange(0, 1000)
    tupla1 += rand
    if tupla1 > tupla:
        maior = tupla1
        menor = tupla
    if tupla1 < menor:
        menor = tupla1
        maior = tupla
    rand = randrange(0, 1000)
    tupla2 += rand
    if tupla2 > maior:
        maior = tupla2
    if tupla2 < menor:
        menor = tupla2
    rand = randrange(0, 1000)
    tupla3 += rand
    if tupla3 > maior:
        maior = tupla
    if tupla3 < menor:
        menor = tupla3
    rand = randrange(0, 1000)
    tupla4 += rand
    if tupla4 > maior:
        maior = tupla4
    if tupla4 < menor:
        menor = tupla4
    if tupla4 > -1:
        break
tupla5 = tupla,tupla1,tupla2,tupla3,tupla4
print(f'Os valores sorteados foram {tupla5}')
print(f'O menor valor sorteado foi {menor} e o maior foi {maior}')







from random import choice
total = 0
um = dez = vinte = cinquenta = cem = 0
lista = [1, 1, 1, 10, 10, 10, 20, 20, 20, 50, 50, 50, 100, 100, 100]
valor = int(input('INFORME QUANTO SERÁ SACADO'))
while total < valor:
    caixa = choice(lista)
    if caixa + total <= valor:
        total += caixa
        if caixa == 1:
            um += 1
        elif caixa == 10:
            dez += 1
        elif caixa == 20:
            vinte += 1
        elif caixa == 50:
            cinquenta += 1
        elif caixa == 100:
            cem += 1
print(f'As células de 1 sacadas foram de {um}\nAs células de 10 sacadas foram de {dez}\nAs células de 20 sacadas foram de {vinte}\nAs células de 50 sacadas foram de {cinquenta}\nAs células de 100 sacadas foram de {cem}')

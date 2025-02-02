from random import randint
from time import sleep
lista = []
def sortea(*num):
    print(f'Sorteando os 5 valores da lista: ',end='')
    for c in range(0,5):
        valor = randint(1,1000)
        lista.append(valor)
        sleep(0.3)
        print(f'{valor} ',end='',flush=True)


def somaPar(*num):
    s = 0
    print()
    print(f'Somando os valores pares de {lista} resultou em ',end='')
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(s)



#Programa Principal
sortea()
somaPar()






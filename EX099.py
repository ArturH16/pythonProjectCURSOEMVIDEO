from time import sleep
def maior(*lista):
    m = 0
    tam = len(lista)
    print('Analisando os valores passados')
    for valor in lista:
        if tam == 1:
            m = valor
        if tam == 0:
            m = 0
        else:
            m = max(lista)
        sleep(0.5)
        print(f'{valor} ',end='',flush=True)
    print(f'Foram informados {len(lista)} valores ao todo')
    print(f'O maior valor informado foi {m}')
    print('-='*20)


#Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

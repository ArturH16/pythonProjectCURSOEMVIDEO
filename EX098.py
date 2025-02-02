from time import sleep
def contador(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2.5)
    if c == 0:
        c = 1
    if c < 0:
        c = -c
    if a < b:
        while a <= b:
            print(f'{a} ',end='',flush=True)
            sleep(0.5)
            a += c
        print()
        print('-='*30)
    else:
        while a >= b:
            print(f'{a} ',end='',flush=True)
            sleep(0.5)
            a -= c
        print()
        print('-='*30)


#Programa Principal
print('-='*30)
contador(1,10,1)
contador(10,0,2)
print('Agora é a vez de você personalizar a contagem!')
pergunta = int(input('Início:'))
pergunta2 = int(input('Fim:'))
pergunta3 = int(input('Passo:'))
contador(pergunta,pergunta2,pergunta3)



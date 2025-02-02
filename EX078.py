lista = []
maior = menor = posicao0 = posicao1 = posicao2 = posicao3 = posicao4 = 0
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
for c,v in enumerate(lista):
    if v == maior:
        print(f'O maior valor foi {maior}')
        print(f'na posição {c}')
    if v == menor:
        print(f'O menor valor que foi {menor}')
        print(f'na posição {c}')


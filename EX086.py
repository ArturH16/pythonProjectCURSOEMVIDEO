lista = [[],[],[],[],[],[],[],[],[]]
for c in range(0,9):
    if c == 0:
        lista[0].append(int(input(f'Adicione um valor na posição [{0,c}]')))
    if c == 1:
        lista[1].append(int(input(f'Adicione um valor na posição [{0,c}]')))
    if c == 2:
        lista[2].append(int(input(f'Adicione um valor na posição [{0,c}]')))
    if c == 3:
        lista[3].append(int(input(f'Adicione um valor na posição [{1,0}]')))
    if c == 4:
        lista[4].append(int(input(f'Adicione um valor na posição [{1,1}]')))
    if c == 5:
        lista[5].append(int(input(f'Adicione um valor na posição [{1,2}]')))
    if c == 6:
        lista[6].append(int(input(f'Adicione um valor na posição [{2,0}]')))
    if c == 7:
        lista[7].append(int(input(f'Adicione um valor na posição [{2,1}]')))
    if c == 8:
        lista[8].append(int(input(f'Adicione um valor na posição [{2,2}]')))
print(f'[  {lista[0]}  ]  [  {lista[1]}  ]  [  {lista[2]}  ]')
print(f'[  {lista[3]}  ]  [  {lista[4]}  ]  [  {lista[5]}  ]')
print(f'[  {lista[6]}  ]  [  {lista[7]}  ]  [  {lista[8]}  ]')

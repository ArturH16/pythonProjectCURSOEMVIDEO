m = [[0,0,0],[0,0,0],[0,0,0]]
par = mai = coluna = 0
for l in range(0,3):
    for c in range(0,3):
        m[l][c]= int(input(f'Digite um valor na posição [{l},{c}]'))
        if m[l][c] % 2 == 0:
            par += m[l][c]
for l in range(0,3):
    coluna += m[l][2]
for c in range(0, 3):
    if c == 0:
        mai = m[1][c]
    if m[1][c] > mai:
        mai = m[1][c]
print(f'[  {m[0][0]}  ] [  {m[0][1]}  ] [  {m[0][2]}  ]')
print(f'[  {m[1][0]}  ] [  {m[1][1]}  ] [  {m[1][2]}  ]')
print(f'[  {m[2][0]}  ] [  {m[2][1]}  ] [  {m[2][2]}  ]')
print('===' * 30)
print(f'A soma dos valores pares resultou em {par}')
print(f'A soma dos valores da terceira coluna resultou em {coluna}')
print(f'O maior valor da segunda linha é {mai}')




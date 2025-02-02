def area(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


# Programa Principal
print('Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (M):'))
comprimento = float(input('COMPRIMENTO (M):'))
area(largura,comprimento)
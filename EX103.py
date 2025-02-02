def ficha(j,g):
    if j == '':
        j = '<desconhecido'
    if g == '' or g not in '123456789':
        g = '0'
    print(f'O jogador {j} fez {g} gol(s) no campeonato')


#Programa Principal
a = str(input('Nome do jogador: '))
b = str(input('Número de gols: '))
ficha(a,b)





















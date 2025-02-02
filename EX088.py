from random import randint
lista =[]
print('='*30)
print('    JOGA NA MEGA SENA    ')
print('='*30)
pergunta = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
jogo = []
while tot <= pergunta:
    c = 0
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            c += 1
        if c == 6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    tot += 1
for p,j in enumerate(lista):
    print(f'Jogo {p + 1}: {j}')




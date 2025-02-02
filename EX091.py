from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
c = 1
jogadores = {'Jogador 1': randint(1,6),'Jogador 2': randint(1,6),'Jogador 3': randint(1,6), 'Jogador 4': randint(1,6)}
print('Valores sorteados')
for k,v in jogadores.items():
    sleep(2)
    print(f'O {k} jogou {v}')
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('Ranking de jogadores')
for k,v in ranking:
    sleep(2)
    print(f'{c} Lugar: {k} com {v}')
    c += 1





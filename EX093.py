dici = {}
gols = []
total = 0
dici['Nome'] = str(input('Nome do jogador'))
dici['Partidas'] = int(input(f'Quantas partidas {dici["Nome"]} jogou?'))
for c in range(0,dici['Partidas']):
    pergunta = int(input(f'Quantos gols na partida {c}?'))
    total += pergunta
    gols.append(pergunta)
    dici['Gols'] = gols
    dici['Total'] = total
print('-='*30)
for k,v in dici.items():
    print(f'{k} recebe {v}')
print('-='*30)
print(f'O jogador {dici["Nome"]} jogou {dici["Partidas"]} partidas')
for p,v in enumerate(gols):
    print(f' Na partida {p}, ele fez {v} gols')
print(f'Foi um total de {dici["Total"]} gols')

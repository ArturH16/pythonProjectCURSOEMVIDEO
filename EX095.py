dici = {}
lista = []
while True:
    partidas = []
    dici['Nome'] = str(input('Nome do jogador '))
    tot = int(input(f'Quantas partidas {dici["Nome"]} jogou?'))
    for c in range(0,tot):
        gols = int(input(f'Quantos gols na partida {c}?'))
        partidas.append(gols)
    dici['Gols'] = partidas
    dici['Total'] = sum(partidas)
    lista.append(dici.copy())
    while True:
        pergunta = str(input('Quer continuar?[S/N]')).strip().upper()
        if pergunta in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if pergunta == 'N':
        break
print('-='*30)
print('Cod ',end='')
for i in dici.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for p,v in enumerate(lista):
    print(f'{p:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    while True:
        resp = int(input('Mostrar dados de qual jogador?(-1 para parar)'))
        if resp > len(lista) - 1:
            print(f'ERRO!Não existe jogador com código {resp}')
        if resp <= len(lista) - 1:
            break
    if resp == -1:
        break
    print(f'Dados de {lista[resp]["Nome"]}')
    for p,v in enumerate(lista[resp]['Gols']):
        print(f'Na partida {p} ele fez {gols} gols')




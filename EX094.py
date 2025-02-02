lista = []
c = a = 0
acima = []
mulheres = []
while True:
    dici = {}
    dici['Nome'] = str(input('Nome:'))
    while True:
        dici['Gênero Biológico'] = str(input('Gênero Biológico[M/F]: ')).strip().upper()
        if dici['Gênero Biológico'] in 'MF':
            if dici['Gênero Biológico'] == 'F':
                mulheres.append(dici['Nome'])
            break
        print('ERRO! Coloque apenas M ou F')
    dici['Idade'] = int(input('Idade: '))
    a += dici['Idade']
    c += 1
    lista.append(dici)
    while True:
        resp = str(input('Quer continuar?[S/N]')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Coloque apenas S ou N')
    if resp == 'N':
        media = a/c
        break
for pessoas in lista:
    if pessoas['Idade'] > media:
        acima.append(pessoas['Nome'])
print('-='*30)
print(f'Ao todo temos {c} pessoas cadastradas\nA média de idade é de {media} anos\nAs mulheres cadastradas foram {mulheres}\nLista das pessoas que estão acima da média de idade: {acima}')
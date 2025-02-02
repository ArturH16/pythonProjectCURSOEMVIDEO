maior = menor = 0
pessoas = []
dados = []
while True:
    pessoas.append(str(input('Qual o nome da pessoa? ')))
    pessoas.append(int(input('Qual o peso da pessoa cadastrada? ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    pergunta = str(input('Quer continuar? S/N ')).strip().upper()
    if pergunta == 'N':
        break
print(f'Total de pessoas cadastradas: {len(dados)}')
print(f'O maior peso foi de {maior}. Peso de',end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print(f'\nO menor peso foi de {menor}. Peso de',end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')




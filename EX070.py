total = c = cont = menor = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto'))
    preco = float(input('Digite o preço do produto em R$:'))
    pergunta = str(input('Quer continuar?: S/N')).strip().upper()
    cont += 1
    total += preco
    if cont == 1:
        preco = menor
        barato = nome
    if preco < menor:
        preco = menor
        barato = nome
    if preco > 1000:
        c += 1
    if pergunta == 'N':
        print(f'O total gasto foi {total:.2f}, a quantidade de produtos acima de R$ 1000 reais é {c} e o produto mais barato foi {barato}')
        break
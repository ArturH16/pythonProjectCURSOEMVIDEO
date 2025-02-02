lista = []
while True:
        r = int(input('Digite um valor:'))
        if r not in lista:
            lista.append(r)
            pergunta = str(input('Quer continuar? S/N')).strip().upper()
        else:
            print('Esse valor já foi adicionado e não será adicionado novamente...')
            pergunta = str(input('Quer continuar? S/N')).strip().upper()
        if pergunta == 'N':
            break
lista.sort()
print(lista)



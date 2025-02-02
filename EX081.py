lista = []
while True:
    lista.append(int(input('Digite um valor')))
    pergunta = str(input('Quer continuar? S/N')).strip().upper()
    if pergunta == 'N':
        break
lista.sort(reverse= True)
print(f'Foram digitados {len(lista)}\n A lista em ordem decrescente é assim: {lista}')
if lista.count(5) >= 1:
    print('O valor 5 está na Lista')
else:
    print('O valor 5 não está na Lista')
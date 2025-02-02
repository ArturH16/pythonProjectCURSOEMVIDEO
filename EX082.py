lista = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor:'))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    pergunta = str(input('Quer continuar? S/N')).strip().upper()
    if pergunta == 'N':
        break
print(f'A lista completa foi {lista}\nA lista dos pares foi {par}\nA lista dos impares foi {impar}')
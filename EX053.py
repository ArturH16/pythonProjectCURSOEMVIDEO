frase = str(input('Digite algo:')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) -1, -1 , -1):
    inverso += juntar[letra]
print(juntar , inverso)
if juntar == inverso:
    print('É PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')


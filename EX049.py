escolha = int(input('Digite a tabuada do número que você quer saber:'))
for c in range(1, 11):
    print('{} x {} = {}'.format(escolha,c,escolha * c))
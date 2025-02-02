somaidade = 0
maior = 0
menor = 0
homemmaisvelho = ''
maioridadedhomem = 0
contadormulher = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    genero = str(input('GÊNERO BIOLÓGICO [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
        if genero == 'M' and idade > maioridadedhomem:
            maioridadedhomem = idade
            homemmaisvelho = nome
        if genero == 'F' and idade < 20:
            contadormulher += 1
m = somaidade / 4
print('A média de idade do grupo é de {}\n O homem mais velho se chama {} e tem {}\n Ao todo são {} mulheres com menos de 20 anos'.format(m,homemmaisvelho,maioridadedhomem,contadormulher))







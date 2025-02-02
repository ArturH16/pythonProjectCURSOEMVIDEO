from ex108 import moeda1

preco = float(input('Digite o preço: R$'))
porcentagem = int(input('Quantos % você quer para aumento e diminuição do preço do produto: '))
print(f'A metade de {moeda1.moeda(preco)} é {moeda1.moeda(moeda1.metade(preco))}\nO dobro de {moeda1.moeda(preco)} é {moeda1.moeda(moeda1.dobro(preco))}\nAumentando {porcentagem}%, temos {moeda1.moeda(moeda1.aumentar(preco,porcentagem))}\nDiminuindo {porcentagem}%, temos {moeda1.moeda(moeda1.diminuir(preco,porcentagem))} ')


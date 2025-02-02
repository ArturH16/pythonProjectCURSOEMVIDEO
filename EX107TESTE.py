from ex107 import moeda

preco = float(input('Digite o preço: R$'))
porcentagem = int(input('Quantos % você quer para aumento e diminuição do preço do produto: '))
print(f'A metade de {preco} é R${moeda.metade(preco)}\nO dobro de {preco} é R${moeda.dobro(preco)}\nAumentando {porcentagem}%, temos R${moeda.aumentar(preco,porcentagem)}\nDiminuindo {porcentagem}%, temos R${moeda.diminuir(preco,porcentagem)} ')
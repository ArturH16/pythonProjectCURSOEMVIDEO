from ex109 import moeda2


preco = float(input('Digite o preço: R$'))
porcentagem = int(input('Quantos % você quer para aumento e diminuição do preço do produto: '))
print(f'A metade de {moeda2.moeda(preco,f=True)} é {moeda2.metade(preco,f=True)}\nO dobro de {moeda2.moeda(preco,f=True)} é {moeda2.dobro(preco,f=True)}\nAumentando {porcentagem}%, temos {moeda2.aumentar(preco,porcentagem,f=True)}\nDiminuindo {porcentagem}%, temos {moeda2.diminuir(preco,porcentagem,f=True)} ')

from ex112.utilidadescev2 import moeda5,dado


preco = dado.leiadinheiro('Digite o preço: R$')
porcentagem = int(input('Quantos % você quer para aumento e diminuição do preço do produto: '))
moeda5.resumo(preco,porcentagem,porcentagem)
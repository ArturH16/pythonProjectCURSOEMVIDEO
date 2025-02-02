preco = float(input('Qual o preço do produto?'))
condicao = float(input('Qual a condição de pagamento?\n Digite 1 para dinheiro ou cheque \n Digite 2 para à vista no cartão \n Digite 3 para em até 2 vezes no cartão \n Digite 4 para três vezes ou mais no cartão'))
if condicao == 1:
    print('O valor a ser pago é de {}'.format(0.9 * preco))
elif condicao == 2:
    print('O valor a ser pago é de {}'.format(0.95 * preco))
elif condicao == 3:
    print('O valor a ser pago é de {}, com parcelas de {}'.format(preco,preco/2))
elif condicao == 4:
    precocomjuros = preco * 1.20
    print('O valor a ser pago é de {}'.format(precocomjuros))


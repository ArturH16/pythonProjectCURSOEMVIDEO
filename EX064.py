pergunta = soma = 0
total = 0
while pergunta != 999:
    pergunta = int(input('Digite um número [999 para parar]'))
    if pergunta != 999:
        soma += pergunta
        total += 1
print('Você digitou {} números e a soma entre eles foi de {}'.format(total,soma))

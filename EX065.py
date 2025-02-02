total = 0
m = 0
maior = menor = 0
pergunta1 = soma = int(input('Digite um valor:'))
total += 1
maior = menor = pergunta1
pergunta2 = str(input('Quer continuar? SIM ou NÃO')).upper().strip()
while pergunta2 == 'SIM':
    pergunta = int(input('Digite um valor:'))
    pergunta2 = str(input('Quer continuar? SIM ou NÃO')).upper().strip()
    soma += pergunta
    total += 1
    m = soma / total
    if total == 1:
        maior = pergunta1
        menor = pergunta1
    else:
        if pergunta > maior:
            maior = pergunta
        if pergunta < menor:
            menor = pergunta
print(' Você digitou {} números e a média foi {:.2f}\n O menor valor foi {} e o maior valor foi {}'.format(total,m,menor,maior))
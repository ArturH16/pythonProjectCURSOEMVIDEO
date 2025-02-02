n = s = 0
while True:
    pergunta = int(input('Digite um valor (999 para parar)'))
    if pergunta == 999:
        break
    s += pergunta
    n+= 1
print(f'Foram digitados {n} valores e a soma foi {s}')

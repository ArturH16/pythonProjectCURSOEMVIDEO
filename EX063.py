n = 0  # Primeiro número da sequência
n2 = 1  # Segundo número da sequência
termos = 1
n3 = 0
pergunta = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))
print(n, end=' → ')
while termos < pergunta:
    print(n2, end=' → ' if termos < pergunta - 1 else '\n')
    n3 = n + n2
    n = n2
    n2 = n3
    termos += 1


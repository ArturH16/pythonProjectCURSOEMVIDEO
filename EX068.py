from random import choice
computador = choice(range(1, 11))
c = 0
escolha = str(input('Escolha par ou impar:')).lower().strip()
escolha1 = int(input('Digite um número:'))
total = escolha1 + computador
while True:
    if escolha == 'par' and total % 2 == 0:
        print(f'Você jogou {escolha1} e o computador {computador}. TOTAL DEU PAR')
        print('Você VENCEU')
        c += 1
        escolha = str(input('Escolha par ou impar:')).lower().strip()
        escolha1 = int(input('Digite um número:'))
    if escolha == 'impar' and total % 2 == 1:
        print(f'Você jogou {escolha1} e o computador {computador}. TOTAL DEU IMPAR')
        print('Você VENCEU')
        escolha = str(input('Escolha par ou impar:')).lower().strip()
        escolha1 = int(input('Digite um número:'))
        c += 1
    if escolha == 'par' and total % 2 == 1:
        print(f'Você jogou {escolha1} e o computador {computador}. TOTAL DEU IMPAR')
        print('Você perdeu...')
        print(f'Você ganhou um total de {c} vezes.')
        break
    if escolha == 'impar' and total % 2 == 0:
        print(f'Você jogou {escolha1} e o computador {computador}. TOTAL DEU PAR')
        print('Você perdeu...')
        print(f'Você ganhou um total de {c} vezes.')
        break

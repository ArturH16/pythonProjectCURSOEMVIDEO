pessoa = int(input('Digite o seu ano de nascimento'))
idade = 2024 - pessoa
alistou = str(input('Já se alistou?')).strip().upper()
if idade == 18 and alistou == 'NÃO':
    print('Já está na hora de você se alistar ao exército!')
elif idade < 18 and alistou == 'NÃO':
    idadecorreta = pessoa + 18 - 2024
    print('Ainda não está na hora de você se alistar ao exército. Seu alistamento será daqui a {} anos'.format(idadecorreta))
elif idade > 18 and alistou == 'NÃO':
    tempoatrasado = 2024 - pessoa + 18
    print('O tempo de alistamento já passou.Você deveria ter se alistado há {} anos'.format(tempoatrasado))
elif idade == 18 or idade > 18 and alistou == 'SIM':
    print('Você está em dia com o exército')
else:
    print('Inválido. Tente novamente')
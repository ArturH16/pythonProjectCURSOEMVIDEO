maior = 0
menor = 0
for pess in range(1 , 8):
    pessoa1 = int(input('Em que ano a {} pessoa nasceu?:'.format(pess)))
    idade = 2024 - pessoa1
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo,{} são maiores de idade \n Ao todo,{} são menores de idade'.format(maior, menor))
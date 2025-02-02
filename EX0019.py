import random
primeiroaluno= input('Digite o nome do primeiro aluno')
segundoaluno= input('Digite o nome do segundo aluno')
terceiroaluno= input('Digite o nome do terceiro aluno')
quartoaluno= input('Digite o nome do quarto aluno')
lista= [primeiroaluno ,segundoaluno,terceiroaluno,quartoaluno]
sort= random.choice(lista)
print('\33[1;32m O escolhido foi {}'.format(sort))
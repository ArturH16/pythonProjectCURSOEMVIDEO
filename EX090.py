aluno = {}
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
print(f'Nome é igual a {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]}')
if aluno['Média'] < 7:
    print('Situação é igual a Reprovado')
else:
    print('Situação é igual a Aprovado')

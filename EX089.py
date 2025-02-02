lista2 = []
pergunta2 = 0
while True:
    nome = str(input('Qual o nome do aluno? '))
    nota1 = float(input('Qual a nota 1 do aluno? '))
    nota2 = float(input('Qual a nota 2 do aluno? '))
    pergunta = str(input('Quer continuar? S/N' )).upper().strip()
    media = ( nota1 + nota2 )/ 2
    lista2.append([nome,media,[nota1,nota2]])
    if pergunta == 'N':
        break
print(f'\n{"NUM":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-'*24)
for p,aluno in enumerate(lista2):
        print(f'{p:<4}{aluno[0]:<10}{aluno[1]:>10.1f}')
while True:
    pergunta2 = int(input('Mostrar notas de qual aluno? [999 INTERROMPE]'))
    if pergunta2 <= len(lista2) - 1:
        print(f'Notas de {lista2[pergunta2][0]} foram: {lista2[pergunta2][2]}')
    if pergunta2 == 999:
        break













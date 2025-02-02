notaum = float(input('Digite a primeira nota do aluno:'))
notadois = float(input('Digite a segunda nota do aluno:'))
media = (notaum + notadois) / 2
if media < 5:
    print('REPROVADO')
elif   5 <= media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!')
c = 0
h = 0
m = 0
while True:
    idade = int(input('Quantos anos essa pessoa tem?:'))
    generobiologico = str(input('Qual o gênero biológico dessa pessoa:')).strip().upper()
    pergunta = str(input('Você quer continuar? Responda S ou N')).strip().upper()
    if idade >= 18:
        c += 1
    if generobiologico == 'M':
        h += 1
    if generobiologico == 'F' and idade < 20:
        m += 1
    if pergunta == 'N':
        break
print(f'{c} pessoas tem mais de 18 anos , {h} homens foram cadastrados e  {m} mulheres tem menos de 20 anos')



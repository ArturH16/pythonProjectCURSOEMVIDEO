par = []
impar = []
todos = []
for c in range(0,7):
    pergunta = int(input('Digite um valor númerico: '))
    if pergunta % 2 == 0:
        par.append(pergunta)
    else:
        impar.append(pergunta)
todos.append(par[:])
todos.append(impar[:])
par.sort()
impar.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {impar}')
print(todos)

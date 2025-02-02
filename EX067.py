while True:
    pergunta = int(input('A tabuada de qual número você quer ver?(Digite um valor negativo para interromper o programa'))
    if pergunta < 0:
        break
    for c in range(1,11):
        print(f'{pergunta} x {c} = {pergunta * c} \n')

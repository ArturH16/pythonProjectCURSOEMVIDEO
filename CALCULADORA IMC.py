x = float(input('Digite sua altura'))
z = float(input('Digite seu peso'))
a = float(z/x**2)
if a < 18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo do peso ideal.'.format(a))
elif 18.5  <= a  <= 24.99:
    print('Seu IMC é de {:.2f}. Você está dentro do peso ideal.'.format(a))
else:
    print('Seu IMC é de {:.2f}. Você está acima do peso ideal'.format(a))



altura = float(input('Qual a sua altura em centímetros?'))
circunferencia = float(input('Qual a sua circunferência em centímetros?'))
formula = circunferencia / altura
if 0.4 <= formula <= 0.49:
    print('SAUDÁVEL')
elif 0.5 <= formula <= 0.59:
    print('SOBREPESO')
else:
    print('SOBREPESO ELEVADO')
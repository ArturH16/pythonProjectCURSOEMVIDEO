name = str(input('Digite seu nome completo:')).strip()
a = name.lower()
b = 'silva' in a
if b== True:
    print('Seu nome tem Silva? True')
else:
    print('Seu nome tem Silva? False')
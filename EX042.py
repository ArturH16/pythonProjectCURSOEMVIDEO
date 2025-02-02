ladoum = float(input('Digite o primeiro segmento:'))
ladodois = float(input('Digite o segundo segmento:'))
ladotres = float(input('Digite o terceiro segmento:'))
if ladoum + ladodois > ladotres:
    print('É POSSÍVEL FORMAR UM TRIÂNGULO')
if ladoum + ladodois < ladotres or ladoum + ladodois == ladotres:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO')
elif ladoum == ladodois and ladoum == ladotres:
    print('TRIÂNGULO EQUILATERO')
elif ladoum != ladodois and ladoum == ladotres:
    print('TRIÂNGULO ISÓSCELES')
elif ladoum != ladodois and ladoum != ladotres:
    print('TRIÂNGULO ESCALENO')
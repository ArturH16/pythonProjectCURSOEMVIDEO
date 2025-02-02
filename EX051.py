print('========== 10 TERMOS DE UMA PA QUE VOCÊ DEFINIR ==========')
num = int(input('Digite o primeiro valor:'))
razao = int(input('Digite a razão:'))
decimotermo= num + (11-1) * razao
for c in range (num,decimotermo,razao):
    numero = num + razao
    print(c)

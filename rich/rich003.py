from rich import print
from rich.table import Table


tabela = Table(title="Tabela de Preços")
tabela.add_column("Nome",justify="left")
tabela.add_column("Salário",justify="center",style="green")

tabela.add_row("Artur"," R$ 10_999")
tabela.add_row("Guanabara","R$ 999_000")

print(tabela)
#Crie a classe ControleRemoto, onde vamos simular o funcionamento de um
#controle simples (canal,volume e liga/desliga)

from rich import print
from rich.panel import Panel

import os

class ControleRemoto:
    def __init__(self):
        self.is_ligada = True
        self.canal_atual = 1
        self.volume = 1


    def controlar_tv(self):
        while True:
            os.system("clear")
            conteudo = "CANAL = "
            if self.is_ligada:
                for c in range(1,6):
                    if c == self.canal_atual:
                        conteudo += f"[white on yellow] {c} [/]"
                    else:
                        conteudo += f" {c} "
                conteudo += f"\nVOLUME = "
                for v in range(1,6):
                    if v <= self.volume:
                        conteudo += "[on green] "
                    else:
                        conteudo += "[on white] "
                tv = Panel(conteudo,title="[TV]")
                print(tv)
            else:
                tv = Panel(":no_entry_sign: [red] A Tv está desligada [/]",title="[TV]")
                print(tv)

            controlar = input(f"< CH{self.canal_atual} >   - VOL{self.volume} + <  ").strip()
            if controlar == "0":
                break
            elif controlar == "@":
                self.is_ligada = not self.is_ligada
            elif controlar == "<":
                if self.canal_atual == 1:
                    self.canal_atual = 5
                else:
                    self.canal_atual -= 1
            elif controlar == ">":
                if self.canal_atual == 5:
                    self.canal_atual = 1
                else:
                    self.canal_atual += 1

            elif controlar == "-":
                if self.volume == 1:
                    continue
                else:
                    self.volume -= 1

            elif controlar == "+":
                if self.volume == 5:
                    continue
                else:
                    self.volume += 1
            else:
                continue














c1 = ControleRemoto()
c1.controlar_tv()


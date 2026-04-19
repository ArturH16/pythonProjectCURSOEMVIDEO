from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():

    a1 = Aluno("José",17,"Informática","T01")
    a1.fazer_aniversario()
    inspect(a1,methods=True)
    a1.fazer_matricula()

    p1 = Professor("Samuel",37,"Biologia","Mestrado")
    p1.fazer_aniversario()
    inspect(p1,methods=True)
    p1.dar_aula()

    f1 = Funcionario("Cláudia",27,"Secretária","Secretaria")
    f1.fazer_aniversario()
    inspect(f1,methods=True)
    f1.bater_ponto()

if __name__ == "__main__":
    main()

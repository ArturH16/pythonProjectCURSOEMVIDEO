from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome,nasc,curso):
        super().__init__(nome,nasc)
        self._curso = curso
        self.cursos_oficiais = ["ADM","ADS","ENG","CONT"]
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")
    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self,curso):
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")
        else:
            self._curso = curso

    def add_curso(self,curso):
        self.cursos_oficiais.append(curso)
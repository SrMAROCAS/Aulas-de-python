class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome
        self.__matricula = matricula
        self.__cpf = cpf
        self.cursos_incritos = [] #Lista de cursos associados ao aluno

    #Método de acesso
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    #Métodos de ação
    def increver_curso(self, curso):
        if curso not in self.cursos_incritos:
            self.cursos_incritos.append(curso)
            curso.adicionar_aluno(self)  # Associa o aluno ao curso

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_incritos:
            lista.append(curso.nome_curso)
        return lista
        
    #Método especial
    def __del__(self):
        print(f"Objeto {self.nome} foi deletado.")     

class Curso:
    def __init__(self, nome_curso):
        self.__nome_curso = nome_curso
        self.alunos_incritos = []

    #Método de acesso
    @property
    def nome_curso(self):
        return self.__nome_curso #(bloqueia direto do atributo)
    
    @nome_curso.setter
    def nome(self, nome_curso):
        self.__nome_curso = nome_curso

    #Métodos de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_incritos:
            self.alunos_incritos.append(aluno)
            aluno.increver_curso(self)  #
    
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_incritos:
            lista.append(aluno.nome)
        return lista
    
    #Método especial
    def __del__(self):
        print(f"Objeto {self.nome_curso} foi deletado.")
        
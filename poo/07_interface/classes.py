#Importações
from abc import ABC
from abc import abstractmethod

#Classe abstrata (interface)
class Pessoa(ABC):
    @abstractmethod
    def __init__(self, email, endereco, telefone):
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    @abstractmethod
    def apresentar(self):
        ...
    @abstractmethod
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Endereço {self.endereco}")
        print(f"Telefone: {self.telefone}")

#Subclasse
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, profissao, email, endereco, telefone):
        self.nome =  nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(email=email, endereco=endereco, telefone=telefone)  
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}"
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Profissao: {self.profissao}")
        super().exibir_dados()
class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj, email, endereco, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, endereco=endereco, telefone=telefone)
    
    def apresentar(self):
        return f"Olá, soomos a empresa{self.nome_fantasia}."
    
    def exibir_dados(self):
        print(f"Razão social: {self.razao_social}")
        print(f"Nome fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()
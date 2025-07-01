from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str

    def __str__(self):
        return f"Olá meu nome é {self.nome}, trabalho com {self.profissao}, meu CPF é {self.cpf}, meu e-mail é {self.email}, meu telefone é {self.telefone} e o meu endereco é {self.endereco}\n"
    
    def __del__(self):
        print(f"Objeto {self.nome} foi deletado com sucesso!")

@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    
    def __str__(self):
        return f"Somos a empresa {self.nome_fantasia}, de Razão Social {self.razao_social}, nosso CNPJ é {self.cnpj}, pode nos contatar pelo e-mail {self.email}, ou por telefone, {self.telefone}, se preferir vá ao nosso endereço {self.endereco}"
    
    def __del__(self):
        print(f"Objeto {self.nome_fantasia} foi deletado com sucesso!\n")
# superclasse ou classe pai

class Pessoa:
    # atributos
    def __init__(self, email, endereco, telefone):
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    #Método
    def exibir_dados(self):
        print(f"E-mail:{self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone {self.telefone}")

# subclasse ou classe filha

class PessoaFisica(Pessoa):
    # atributos
    def __init__(self, nome, cpf, profissao, genero, email, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        self.genero = genero
        super().__init__(email=email, endereco=endereco, telefone=telefone)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.profissao}")
        print(f"Gênero: {self.genero}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj, email, endereco, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, endereco=endereco, telefone=telefone)

    def exibir_dados(self):
        print(f"Razão Social: {self.razao_social}")
        print(f"Nome fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()
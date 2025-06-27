class Pessoa:
    def __init__(self, email, telefone):
        self._email = email # Atributo privado
        self._telefone = telefone  # Atributo privado

    #Método get
    @property
    def email(self):
        return self._email
    
    #Método set
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
    
class PessoaFisica(Pessoa):
        def __init__(self, nome, cpf, profissao, email, telefone):
            self._nome = nome
            self._cpf = cpf
            self._profissao = profissao
            super().__init__(email=email, telefone=telefone)
        @property
        def nome(self):
            return self._nome
        
        @nome.setter
        def nome(self, nome):
            self._nome = nome
        
        @property
        def cpf(self):
            return self._cpf
        
        @cpf.setter
        def cpf(self, cpf):
            self._cpf = cpf
        
        @property
        def profissao(self):
            return self._profissao
        
        @profissao.setter
        def profissao(self, profissao):
            self._profissao = profissao

class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj, email, telefone):
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        super().__init__(email=email, telefone=telefone)
    
    @property
    def razao_social(self):
        return self._razao_social
    
    @razao_social.setter
    def razao_social(self, razao_social):
        self._razao_social = razao_social
    
    @property
    def nome_fantasia(self):
        return self._nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self._nome_fantasia = nome_fantasia
    
    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj
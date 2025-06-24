import random

#Classe
class Pessoa:
    def __init__(self, nome, email, profissao, humor):
        self.nome = nome 
        self.email = email 
        self.profissao = profissao
        self.humor = humor

    #Métodos
    def dar_boas_vindas(self):
        return "Olá, boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. É um prazer!"
    
    def perguntar(self):
        return f"Qual o seu nome?"
    
    def cartao_de_visita(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"profissão: {self.profissao}")

    def ofender(self):
        return f"Quem liga? Me erra! Vai ver se eu tô na esquina!"

#Algoritmo principal
if __name__ == "__main__":
    #Instancia de dois objetos da mesma classe
    usuario_masculino = Pessoa("", "", "", bool(random.getrandbits(1))) 
    usuario_feminino = Pessoa("", "", "", bool(random.getrandbits(1)))

    #Seta os valores dos atributos do objeto masculino
    usuario_masculino.nome = input("Informe seu nome: ")
    usuario_masculino.email = input("Informe seu e-mail: ")
    usuario_masculino.profissao = input("Informe sua profissão: ")

    #Seta os valores dos atributos do objeto masculino
    usuario_feminino.nome = input("Informe seu nome: ")
    usuario_feminino.email = input("Informe seu e-mail: ")
    usuario_feminino.profissao = input("Informe sua profissão: ")

    print(f"Homen: - {usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: - {usuario_feminino.dar_boas_vindas()}")
    print(f"Homen: - {usuario_masculino.perguntar()}")
    if usuario_feminino.humor is True:
        print(f"Mulher: - {usuario_feminino.cumprimentar()}")
        print(f"Mulher -  {usuario_feminino.perguntar()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homen: - {usuario_masculino.cumprimentar()}")
        print(f"Homen: Bom humor = {usuario_masculino.humor}")
        print("Segue meu cartão de visistas: ")
        print(usuario_masculino.cartao_de_visita())
    else:
        print(f"Mulher: -{usuario_feminino.ofender()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homen Bom humor = {usuario_masculino.humor}")
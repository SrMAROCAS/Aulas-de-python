#Class
class Pessoa:
    #Atributos
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

    #Métodos (sempre que declarar um método, deve-se declarar o parâmetro self)
    def apresentar(self):
        print(f"\nOlá, meu nome é {self.nome}, tenho {self.idade} anos, trabalho como {self.profissao} e meu e-mail é {self.email}.\n")

#Algoritmo principal
if __name__ == "__main__":
    # Instancia a classe Pessoa 
    usuario = Pessoa()

    #Executar o método
    usuario.apresentar()
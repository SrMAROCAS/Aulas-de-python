# classe
class Pessoa:
    #Método construtor
    def __init__(self, nome, idade, email, profissao):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao

    #Método de ação
    def apresentar(self):
        print(f"Olá, eu me chamo {self.nome}, tenho {self.idade} anos, trabalho como {self.profissao} e meu e-mail é {self.email}.")

#Algoritmo principal
if __name__ == "__main__":
    usuario = Pessoa("", 0, "", "")
    try:
        #Seta valores aos atributos do objeto
        usuario.nome = input("Informe o nome do usuário: ").title().strip()
        usuario.idade = int(input("Informe a idade: "))
        usuario.email = input("Informe o e-mail: ").lower().strip()
        usuario.profissao = input("informe sua profisssão: ").strip

        #Executar o método
        usuario.apresentar()
    except Exception as e:
        print(f"Não foi possível executar o programa. {e}.")

'''
Atividade: Crie um programa que receba os dados de dois objetos diferentes da mesma classe Pessoa. Os daddos serão os seguintes: 
- Nome
- Idade
- E-mail
- Telefone
- Gênero
- Tipo sanguíneo
- Já teve doença transmitida por sangue?
Suponha que o objeto'usuário_2' esteja precisando de doação de sangue do 'usuario_1'. O programa deve informar os dados dos dois usuários,
e ao final, informar se o usuario_1 pode doar sangue para o usuario_2 ou não:
NOTE As duas últimas perguntas deberão ter uma resposta randônica.
'''

#Bibliotecas
import random
import os

#Classe
class Pessoa:
    def __init__(self, nome, idade, email, telefone, genero, tipo_sanguineo, ist):
        self.nome = nome 
        self.idade = idade
        self.email = email 
        self.telefone = telefone
        self.genero = genero
        self.tipo_sanguineo = tipo_sanguineo
        self.ist = ist
#Lista de tipod sanguíneos       
tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

#Algoritmo principal
if __name__ == "__main__": 
     #Instancia de dois objetos da mesma classe
    usuario_1 = Pessoa("", 0, "", "", "", random.randint(0, 8), bool(random.getrandbits(1)) ) 
    usuario_2 = Pessoa("", 0, "", "", "", bool(random.getrandbits(1)), bool(random.getrandbits(1)))
    
    usuario_1.nome = input("Informe o nome do doador: ").title().strip()
    usuario_1.idade = int(input("Informe a idade do doador: ").strip())
    usuario_1.email = input("Informe o e-mail do doador: ").lower().strip()
    usuario_1.telefone = input("Informe o telefone do doador: ").strip()
    usuario_1.genero = input("Informe o gênero do doador: ").title().strip()
    os.system("cls" if os.name == "nt" else "clear")
   

    #Seta os valores dos atributos do objeto masculino
    usuario_2.nome = input("Informe o nome do receptor do sangue: ").title().strip()
    usuario_2.idade = int(input("Informe a idade do receptor do sangue: ").strip())
    usuario_2.email = input("Informe o e-mail do receptor do sangue: ").lower().strip()
    usuario_2.telefone = input("Informe o telefone do receptor do sangue: ").strip()
    usuario_2.genero = input("Informe o gênero do receptor do sangue: ").title().strip()
    
    if usuario_1.tipo_sangue == usuario_2.tipo_sangue and usuario_1.ist == False:
        print(f"A compatibilidade sanguínea entre {usuario_1.nome} e {usuario_2.nome} é adequada para a doação.")

    else:
        print(f"A compatibilidade sanguínea entre {usuario_1.nome} e {usuario_2.nome} não é adequada para a doação.")
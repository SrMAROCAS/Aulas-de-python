'''
# TODO - Atividade 08
Crie um programa onde o usuário possa fazer as seguintes opções:
- Calculr a área de um quadrado;
- Calcular a área de um retângulo;
- Calcular a área de um triângulo;
- Calcular a área de um trapézio;
- Sair do programa;
 # NOTE -  O usuário deverá escolher a operação em um menu
 # NOTE - O programa deverá ser feito com funções
 '''
import os
import math as m

def bem_vindo (nome):
    return f"Seja bem-vindo {nome}!!!" 

nome = input("Informe seu nome: ")
print (bem_vindo(nome))
input("Aperte enter para iniciar o menu...\n")

os.system("cls" if os.name == "nt" else "clear")

while True:
    print(f"{'-'*30} MENU {'-'*30}\n")
    print("1 - Calculr a área de um quadrado")
    print("2 - Calcular a área de um retângulo")
    print("3 - calcular a área de um trinângulo")
    print("4 - calcular a área de um trapézio")
    print("5 - Sair do programa")
    print(f"\n{'-'*66}\n")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            ...
        case "1":
            ...
        
        
    
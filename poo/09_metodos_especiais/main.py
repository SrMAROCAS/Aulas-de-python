from classes import Pessoa
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    #Instancia classe
    usuario = Pessoa(nome="", profissao="", idade=0)

    while True:
        print("1 - Inserir dados e exibir")
        print("2 - Sair do programa")
        opcao = input("Escolha uma opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                try:
                    usuario.nome = input("Informe o nome: ").strip().title()
                    usuario.idade = int(input("Informe a idade: "))
                    usuario.profissao = input("Informe a profissao: ").strip().title()
                
                    limpar()
                    
                    #Exibe dados
                    print(usuario)
                    print(f"Idade de: {usuario.nome}: {len(usuario)} anos")
                    continue
                except Exception as e:
                    print(f"Não foi foi possível executar o prgrama. {e}.")
                    break
            case "2":
                break
            case _:
                print("Opção inválida")
                continue
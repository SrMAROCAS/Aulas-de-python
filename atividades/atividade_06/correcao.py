import os
usuario = {} # se eu inserir no laço de repetção, o dicionário será reiniciado a cada iteração

while True: 
    print(f"{'-'*20} MENU {'-'*20}\n")
    print("1 - Cadastrar nova chave")
    print("2 - Exibir dados do usuário")
    print("3 - Alterar valor da chave")
    print("4 - Excluir chave")
    print("5 - Sair do programa")

    opcao = input("Informe a opção desejada: ")
    os.system("cls")
    match opcao:
        case"1":
            chave = input("Informe o nome da chave que deseja inserir: ").lower().strip()
            usuario[chave] = input(f"Informe o valor para a chave '{chave}': ")

            print("Chave cadastrada com sucesso!")
            continue
        case"2":
            for chave in usuario:
                print(f"{chave.capitalize()}: {usuario[chave]}")
            print("\n")
            continue
        case"3":
            chave = input("Informe o nome da chave que deseja alterar: ").lower().strip()
            if chave in usuario:
                usuario[chave] = input(f"Informe o novo valor para a chave '{chave}': ")
                print(f"Chave '{chave}' alterada com sucesso!")
            else:
                os.system("cls")
                print(f"A chave '{chave}' não foi encontrada.")
            continue
        case"4":
            chave = input("Informe o nome da chave que deseja excluir: ").lower().strip()
            confirmacao = input(f"Tem certeza que deseja excluir a chave '{chave}'? (s/n): ").lower().strip()
            os.system("cls")
            if confirmacao is "s": #possso colocar is ou ==, ambos funcionam
            
                del usuario[chave]
                print(f"Chave '{chave}' excluída com sucesso!")
            else:
                print("Chave não foi excluída.")
        case"5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
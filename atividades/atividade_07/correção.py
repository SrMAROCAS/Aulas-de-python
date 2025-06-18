# Biblioteca 
import os

# Lista
usuarios = []

while True:
    # Menu
    print(f"{'-'*20} Bem-vindo {'-'*20}")
    print("1 - Inserir dados de novo usuário")
    print("2 - Exibir lista de usuários")
    print("3 - Alterar dados de um usuário já cadastrado")
    print("4 - Excluir usuário da lista")
    print("5 - Sair do programa")
    opcao = input("Informe a opção desejada: ")
    os.system("cls") # para rodar no sistema lin ux os.system("cls" if os.name == "nt" else "clear") 
    match opcao:
        case "1":
            #inicializa o dicionário
            usuario = {}
            # Input do usuário
            usuario['nome'] = input("Informe o nome: ").title().strip()
            usuario['data_nascimento'] = input("Informe a data de nascimento (DD/MM/AAAA): ").strip()
            usuario['email'] = input("Informe o e-mail: ").strip()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['telefone'] = input("Informe o telefone: ").strip()
            usuario['profissao'] = input("Informe a profissão: ").strip()
            usuario['genero'] = input("Informe o gênero: ").strip()
            os.system("cls" if os.name == "nt" else "clear")
            try:
                # Inserir os daos do usuário na lista
                usuarios.append(usuario)
                print("Usuário cadastrado com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir novo usuário: {e}")
            finally:
                continue
        
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLista de Usuários:")
            for i in range(len(usuarios)):
                print(f"{'-'*40}")
                print(f"Índice: {i}.")
                for chave in usuarios[i]:
                    print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
            continue
        case "3":
            try:
                i = int(input("Informe o índice desejado: "))
                if i >= 0 and i < len(usuarios):
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    chave_escolhida = input("Informe a chave que deseja alterar: ").strip().lower()
                    usuarios[i][chave_escolhida] = input("Informe o novo valor: ").strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print("chave alterada com sucesso!")
                else: 
                    print("Índice inválido.")
                    continue
            except Exception as e:
                print(f"não foinpossível alterar dados. {e}.")
            finally:
                continue
        case "4":
            try:
                i = int(input("Informe o índice: "))
                if i >= 0 and i < len(usuarios):
                    for chave in usuario[i]:
                        print(f"{chave.capitalize()}: {usuario[i].get(chave)}")
                confirma = input("Tem certeza de que deseja excluir este usuário? (s/n)").strip().lower()
                match confirma:
                    case "s":
                        del(usuario[i])
                        os.system("cls"if os.name == "nt" else "clear")
                        print("Usuário deletado com sucesso.")
                    case "n":
                        os.system("cls"if os.name == "nt" else "clear")
                    case _:
                         os.system("cls"if os.name == "nt" else "clear")
                         print("Opção inválida. Operação cancelada.")

                else: 
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível execluir usuário. {e}.")

        case "5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
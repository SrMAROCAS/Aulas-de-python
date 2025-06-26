#Importações
import classes
import os

if __name__ == "__main__":
    #Instancia objeto
    usuario = classes.PessoaFisica("", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "") 

    while True:
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados da empresa")
        print("3 - Exibir os dados")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")

        match opcao:
            case "1":
                try: 
                    usuario.nome = input("Informe o nome do usuário: ").title().strip()
                    usuario.cpf = input("Informe o CPF: ").strip()
                    usuario.profissão = input("Informe a profissao: ").strip()
                    usuario.email = input("Informe o e-mail: ").strip().lower()
                    usuario.endereco = input("Informe o endereço: ").strip().title()
                    usuario.telefone = input("Informe o telefone: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"Dados do {usuario.nome} inseridos com sucesso!")

                except Exception as e:
                    print(f"Não foi possível inserir dados do usuário. {e}.")
                finally:
                    continue
            case"2":
                try:
                    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
                    empresa.nome_fantasia = input("Informe a nome da empresa: ").title().strip()
                    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
                    empresa.email = input("Informe o e-mail da empresa: ").lower().strip()
                    empresa.endereco = input("Informe o endereço da empresa: ").title().strip()
                    empresa.telefone = input("Informe o telefone da empresa: ").strip()
                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados da empresa {empresa.nome_fantasia} inseridos com sucesso!")

                except Exception as e:
                    print(f"Não foi possível inserir dados do usuário. {e}.")
                finally:
                    continue
            case "3":
                try:
                    print(f"{'-'*20} Dados do Usuário {'-'*20}")
                    usuario.exibir_dados()
                    print(f"{'-'*20} Dados da Empresa {'-'*20}")
                    empresa.exibir_dados()
                    
                except Exception as e:
                    print(f"Não foi possível exibir os dados. {e}.")
                finally:
                    continue
                '''
            case "3":
                if not usuario.nome or not empresa.razao_social:
                    print("Por favor, insira os dados do usuário e da empresa antes de exibir.")
                    input("Pressione Enter para continuar...")
                    print("\n")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                print(usuario.apresentar())
                usuario.exibir_dados()
                print("\n")
                print(empresa.apresentar())
                empresa.exibir_dados()
                input("Pressione Enter para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
             '''
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida")
                continue

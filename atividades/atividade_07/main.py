'''
Atividade 07 - 
Crie um programa que faça as seguintes operações:
- Inserir dados de um novo usuário
- Exibir lista de usuários
- Alterar dados de um usuário já cadastrado
- Excluir usuário da lista
- Sair do programa

Os dadps a serem cadastrados serão os seguintes:
- Nome
- Data de nascimento
- E-mail
- CPF
- Telefone
- Profissão
- Gênero
'''
import os

chaves = [
    'Nome',
    'Data de nascimento (DD/MM/AAAA)',
    'E-mail',
    'CPF',
    'Telefone',
    'Profissão',
    'Gênero'
]

while True: 

	os.system("cls")
	usuarios = {}
	print(f"{'-'*25} Bem-vindo {'-'*25}\n")
	print("1 - Inserir dados de um novo usuário")
	print("2 - Exibir lista de usuários")
	print("3 - Pesquisar usuário na lista")
	print("4 - Alterar usuário da lista")
	print("5 - Excluir usuário da lista")
	print("6 - Sair do programa")
	print(f"\n{'-'*30}-{'-'*30}\n")

	opcao = input("Qual das opções acima você gostaria de realizar? ").strip()
	os.system("cls")
	
	match opcao:
		case "1":
			for chave in chaves:
				usuarios[chave.lower()] = input(f"Informe {chave}: ")
				usuarios.append(usuarios)
			continue
		case "2":
			print(f"\n{'-'*25} Bem-vindo {'-'*25}\n")
			for dado in usuarios:
				print(f"{dado}: {usuarios[dado]}")
			continue

		case "3":
			...
			continue
		case "4":
			nome = input("Informe o nome do usuário que deseja alterar: ").strip().lower()
			if nome in usuarios:
				nome = input("Informe o nome do usuário que deseja alterar os dados: ").strip().lower()
				...
			else:
				print(f"O usuário '{nome}' não foi encontrado.")
			continue
		case "5":
			nome = input("Informe o nome do usuário que deseja excluir: ").strip().lower()
			if nome in usuarios:
				confirmacao = input(f"Tem certeza que deseja excluir o usuário '{nome}'? (s/n): ").strip().lower()
				os.system("cls")
				if confirmacao == "s":
					del usuarios[nome]
					print(f"Usuário '{nome}' excluído com sucesso!")
				else:
					print("Usuário não foi excluído.")
			else:
				print(f"O usuário '{nome}' não foi encontrado.")
			continue

		case "6":
			print("Encerrando o programa...")
			break
		case _:
			print("Opção inválida. Tente novamente.")
			continue
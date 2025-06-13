# TODO - atividade

# Crie um programa em que o usuário pode escolher entre:
# - inserir um nome em uma lista
# - exibir a lista de nomes
# - pesquisar por um nome na lista
# - Alterar item da lista
# - Excluir item da lista 
# - sair do programa

import os #permitir limpar o terminal
nomes = []

while True: # Loop infinito para manter o menu ativo
	print(f"{'-'*30} MENU {'-'*30}")
	print("1 - Inserir novo nome na lista")
	print("2 - Exibir lista")
	print("3 - Pesquisar nome na lista")
	print("4 - Alterar um item na lista")
	print("5 - Excluir item da lista")
	print("6 - Sair do programa")
	print(f"{'-'*30} ---- {'-'*30}")

	opcao = input("Opção desejada: ").strip()
	
	os.system("cls")

	match opcao:
		case "1":
			novo_nome = input("Informe o nome a ser cadastrado: ").strip().title()
			os.system("cls")
			try:
				nomes.append(novo_nome)
				print(f"{novo_nome} inserido com sucesso!")
			except Exception as e:
				print("Não foi possivel inserir o nome na lista. {e}.")
			finally:
				continue
		case"2":
			print("\nLista:\n")
			try:
				for i in range(len(nomes)):
					print(f"Índice: {i}: {nomes[i]}.")
				print("\n")
			except Exception as e:
				print("Não foi possivel exibir o nome na lista. {e}.")
			finally:
				continue
		case"3":
			nome_pesquisado = input("Informe o nome a ser pesquisado: ").title().strip()
			os.system("cls")
			result = nomes.count(nome_pesquisado)
			print(f"{nome_pesquisado} foi encontrado {result} vezes.")
			continue
		case"4":
			try: 
				i = int(input("Informe i índice que deseja alterar: "))
				if i >= 0 and i < len(nomes):
					nomes[i] = input("informe o novo nome: ")
					print("Nome alterado com sucesso.")
				else:
					print("Índice inválido.")
			except Exception as e:
				print(f"Não foi possível alterar item da lista. {e}.")
			finally:
				continue
		case"5":
			try:
				i = int(input("Informe o índice que deseja excluir: "))
				if i >= 0 and i < len(nomes):
					del(nomes[i])
					print("Nome excluído com sucesso.")
				else:
					print(f"Não foi possível excluir nome. {e}.")
			except Exception as e:
				print(f"Não foi possível excluir nome. {e}.")	
			finally:
				continue
		case"6":
			print("Programa encerrado!")
		case _:
			print("Opção inválida")
			continue
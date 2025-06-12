# TODO - atividade

# Crie um programa em que o usuário pode escolher entre:
# - inserir um nome em uma lista
# - exibir a lista de nomes
# - pesquisar por um nome na lista
# - sair do programa

import os #permitir limpar o terminal
nomes = []

while True: # Loop infinito para manter o menu ativo
	print(f"{'-'*30} MENU {'-'*30}")
	print("1 - Inserir novo nome na lista")
	print("2 - Exibir lista")
	print("3 - Pesquisar nome na lista")
	print("4 - Sair do programa")
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
				for nome in nomes:
					print(nome)
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
			print("Programa encerrado!")
		case _:
			print("Opção inválida")
			continue
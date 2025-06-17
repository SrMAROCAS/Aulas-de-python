"""
Atividade: Crie um programa com um dicionário chamado 'usuario' como o seguinte menu:
- Cadastrar nova chave
- Exibir dados do usuário
- Alterar valor da chave
- Excluir chave
- Sair do programa
# Note - os dados a serem inseridos tem a ver com dados do usuário
"""
import os
usuario = {

}

while True: # Loop infinito para manter o menu ativo
	print(f"{'-'*30} MENU {'-'*30}")
	print("1 - Cadastrar nova chave")
	print("2 - Exibir dados do usuário")
	print("3 - Alterar valor da chave")
	print("4 - Excluir chave")
	print("5 - Sair do programa")
	print(f"{'-'*30} ---- {'-'*30}")

	opcao = input("Informe a opção desejada: ").strip().title()
	
	os.system("cls")

	match opcao:
		case "1":
			chave = input("Informe o nome da chave a ser cadastrada: ").strip().lower()
			if chave not in usuario:
				valor = input(f"Informe o valor para a chave '{chave}': ").strip()
				usuario[chave] = valor
				print(f"Chave '{chave}' cadastrada com sucesso!")
			else:
				print(f"A chave '{chave}' já existe.")
			continue
		case "2":
			if usuario:
				print("\nDados do usuário:")
				for chave, valor in usuario.items():
					print(f"{chave.capitalize()}: {valor}")
			else:
				print("Nenhum dado cadastrado.")
			continue
		case "3":
			chave = input("Informe o nome da chave que deseja alterar: ").strip().lower()
			if chave in usuario:
				novo_valor = input(f"Informe o novo valor para a chave '{chave}': ").strip()
				usuario[chave] = novo_valor
				print(f"Chave '{chave}' alterada com sucesso!")
			else:
				print(f"A chave '{chave}' não foi encontrada.")
			continue
		case "4":
			chave = input("Informe o nome da chave que deseja excluir: ").strip().lower()
			if chave in usuario:
				del usuario[chave]
				print(f"Chave '{chave}' excluída com sucesso!")
			else:
				print(f"A chave '{chave}' não foi encontrada.")
			continue
		case "5":
			print("Saindo do programa...")
			break
		case _:
			print("Opção inválida. Tente novamente.")

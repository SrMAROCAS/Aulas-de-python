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
usuarios = {}
chaves = [
    'Nome',
    'Data de nascimento',
    'E-mail',
    'CPF',
    'Telefone',
    'Profissão',
    'Gênero'
]
while True:  # Loop infinito para manter o menu ativo
    print(f"{'-'*30} Bem-vindo {'-'*30}")
    print("1 - Inserir dados de um novo usuário")
    print("2 - Exibir lista de usuários")
    print("3 - Pesquisar usuário na lista")
    print("4 - Alterar usuário da lista")
    print("5 - Excluir usuário da lista")
    print("6 - Sair do programa")
    print(f"{'-'*35}-{'-'*35}")

    opcao = input("Qual das opções acima você gostaria de realizar? ").strip()
    os.system("cls")

    match opcao:
        case "1":
            usuario = {}
            for chave in chaves:
                valor = input(f"Informe o {chave}: ").strip()
                usuario[chave.lower()] = valor
            usuarios[usuario['nome'].lower()] = usuario
            print("Usuário cadastrado com sucesso!")
            continue
        case "2":
            if usuarios:
                for nome, dados in usuarios.items():
                    print(f"\nUsuário: {nome.capitalize()}")
                    for chave, valor in dados.items():
                        print(f"{chave.capitalize()}: {valor}")
            else:
                print("Nenhum usuário cadastrado.")
            continue
        case "3":
            nome = input("Informe o nome do usuário a ser pesquisado: ").strip().lower()
            if nome in usuarios:
                dados = usuarios[nome]
                print(f"\nUsuário: {nome.capitalize()}")
                for chave, valor in dados.items():
                    print(f"{chave.capitalize()}: {valor}")
            else:
                print(f"Usuário '{nome}' não encontrado.")
            continue
        case "4":
            nome = input("Informe o nome do usuário a ser alterado: ").strip().lower()
            if nome in usuarios:
                usuario = usuarios[nome]
                for chave in chaves:
                    novo_valor = input(f"Informe o novo {chave} (deixe em branco para manter '{usuario[chave.lower()]}'): ").strip()
                    if novo_valor:
                        usuario[chave.lower()] = novo_valor
                print(f"Usuário '{nome}' alterado com sucesso!")
            else:
                print(f"Usuário '{nome}' não encontrado.")
            continue
        case "5":
            nome = input("Informe o nome do usuário a ser excluído: ").strip().lower()
            if nome in usuarios:
                confirmacao = input(f"Tem certeza que deseja excluir o usuário '{nome}'? (s/n): ").strip().lower()
                if confirmacao == 's':
                    del usuarios[nome]
                    print(f"Usuário '{nome}' excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")
            else:
                print(f"Usuário '{nome}' não encontrado.")
            continue
"""
Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista
- Exibir a lista de nomes
- Pesquisar por um nome na lista
- Alterar item da lista
- Excluir item da lista 
- Sair do programa
"""

lista = []
print("----------Menu---------")
print("1. Inserir um nome na lista") 
print("2. Exibir a lista de nomes")
print("3. Pesquisar por um nome na lista")
print("4. Sair do programa")
opção = input("Digite a opção desejada: ").strip()
while True:
    if opção == "1":
        nome = input("Digite o nome a ser inserido: ").strip()
        lista.append(nome)
        print(f"{nome} foi adicionado à lista.")
    elif opção == "2":
        if lista:
            print("Lista de nomes:")
            for nome in sorted(lista):  # Ordena a lista antes de exibir
                print(nome)
        else:
            print("A lista está vazia.")
    elif opção == "3":
        nome = input("Digite o nome a ser pesquisado: ").strip()
        if nome in lista:
            print(f"{nome} está na lista.")
        else:
            print(f"{nome} não foi encontrado na lista.")
    elif opção == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
    
    opção = input("Digite a opção desejada: ").strip()


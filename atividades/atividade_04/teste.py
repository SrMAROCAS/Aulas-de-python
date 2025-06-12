"""
Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista
- Exibir a lista de nomes
- Pesquisar por um nome na lista
- Sair do programa
"""

lista = []

print("----------Menu---------")
print("1. Inserir um nome na lista")
print("2. Exibir a lista de nomes")
print("3. Pesquisar por um nome na lista")
print("4. Sair do programa")

opção = input("Digite a opção desejada: ").capitalize().strip() 

whilwe True:
if opção not in ["1", "2", "3", "4"]:
    print("Opção inválida. Tente novamente.")
    opção = input("Digite a opção desejada: ").capitalize().strip()
    continue
if opção == "1":
    nome = input("Informe o nome do item que você deseja que seja adicionado: ").capitalize().strip().title()
    lista.append(nome) # Adiciona o item à lista carrinho
    print(f"{nome} inserido no carrinnho com sucesso!")
    confirmar = input("Deseja inserir outro item na lista? (s/n): ").strip().lower()
match confirmar:
    case "s": 
       
        continue
    case "n":
        print("Itens do carrinho:")
        for item in carrinho: # Exibe os itens do carrinho
            print(item)
        break

    lista.sort() 
continue
for nome in lista: # Exibe os itens do carrinho
    print(nome)

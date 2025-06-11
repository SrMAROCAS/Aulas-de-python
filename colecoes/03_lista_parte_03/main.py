## Declaração de lista
carrinho = [] # Lista vazia

while True: # Loop infinito
    item = input("Informe o item: ").capitalize().strip()  
    carrinho.append(item) # Adiciona o item à lista carrinho
    print(f"{item} inserido no carrinnho com sucesso!")
    confirmar = input("Deseja inserir outro item? (s/n): ").strip().lower() # Pergunta se o usuário deseja continuar
    match confirmar:
        case "s": 
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            continue
    
# Ordena a lista carrinho em ordem alfabética  
carrinho.sort() 

for item in carrinho: # Exibe os itens do carrinho
    print(item)
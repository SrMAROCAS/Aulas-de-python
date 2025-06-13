# Tuplas
estados = (
    "Distrito Federal",
    "Goiás",
    "Minas Gerais",
    "Tocantins",
    "Rio de Janeiro",
    "Cerará",
)

# Listar a tupla
for estado in estados:
    print(estado)

# Pesquisando estados
estado_pesquisa = input("Informe um estado que deseja pesquisar: ").title().strip()
qtde_estados = estados.count(estado_pesquisa)

print(f"{estado_pesquisa} foi encontrado {qtde_estados} vezes na tupla.")

# Tentando acrescentar item na tupla
novo_estado = input("Informe o nome do estado que deseja inserir: ")
estados.append(novo_estado)
for estado in estados:
    print(f"{estado_pesquisa} foi encontrado {qtde_estados} vezes na tupla.")

# Tentando organizar a tupla em ordem alfabética
try: 
    estados.sort()
    for estado in estados:
        print(estado)
except Exception as e:
    print(f"Não foi possível ordenar a tupla. {e}.")


# Importar biblioteca
import os

#Lista
frutas = [
    "Morango",
    "Banana",
    "Maçã",
    "Pera",
    "Uva",
    "Maracuja",
    "Abacaxi",
    "Laranja",
    "Pêssego"

]

"""
# Mudadando pera para mamão
frutas[3] = "Mamão" #descobrir o indice da fruta que deseja mudar

#exibe a lista
for fruta in frutas:
    print(fruta)
"""

## Usuário escolhe a fruta que ele quer mudar
# Exibir a lista com seus respectivos índices
for i in range(len(frutas)):
    print(f"Índice {i+1}: {frutas[i]}.")

# Usuário informa o índice da fruta que deseja alterar
try:
    indice = int(input("Informe o número do índice a ser alterado: "))
    os.system ("cls")
    if indice >= 1 and indice < len(frutas):
        print(f"Valor encontrado: {frutas[indice]}.")
        frutas[indice] = input("Informe o nome da nova fruta: ")
        os.system ("cls")
        print("Fruta alterada com sucesso\n")
    else:
        print("Valor do índice inválido.")
except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")
finally:
    print("\nNova lista:\n")
    for indice in range(len(frutas)):
        print(f"Índice {indice+1}: {frutas[indice]}.")


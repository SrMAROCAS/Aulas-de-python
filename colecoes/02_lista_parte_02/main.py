# Declaração de lista
cidades = ["Brasília", "Rio de Janeiro", "Goiânia", "São Paulo", "Palmas"]

## Exibindo a lista
for i in range(len(cidades)): # i é um contador u o range é uma função de repetição eo olen conta quantos elementos tem a lista automaticamente
    print(f"{i + 1}° {cidades[i]}") # Exibe o número do elemento e o nome da cidade, o i + 1 é para começar a contagem do 1 e não do 0
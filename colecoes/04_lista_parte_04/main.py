#Lista de cidades 
cidades = [
    "Brasília", 
    "Rio de Janeiro", 
    "Goiânia",
    "São Paulo", 
    "Palmas"
    "São Luís",
    "Belém",
    "Fortaleza",
    "Salvador",
    "porto Alegre",
    "Florianópolis",
    "Belo Horizonte",
    "Marceió",
    "Brasília",
    "Florianópolis",
    "Marceió",
    "Goiânia",
    "Brasília"
]

#Usuário faz a pesquisa
pesquisa = input("informe o nome da cidade a ser pesquisada: ").strip().title()

#if pesquisa in cidades:  # Ou seja se o valor de pesquisa estiver na lista cidades
    #print(f"{pesquisa} encontrado!")
#else:
    #print(f"{pesquisa} não encontrado.")

quantidade = cidades.count(pesquisa)  # Conta quantas vezes o valor de pesquisa aparece na lista cidades
print(f"{pesquisa} foi encontrado {quantidade} vezes na lista de cidades.")
  
# Dicionário - É uma lista identificada por chaves, onde cada chave é única e associada a um valor. É uma estrutura de dados que permite armazenar pares de chave-valor.
pessoa = {
    'nome': "Bianca Cristina",
    'idade': 20,
    'email': "biancacalopes@gmail.com",
    'cpf' : "123.456.789-00",
}

# Exibindo o dicionário
for dado in pessoa:
    print(f"{dado.capitalize()}: {pessoa.get(dado)}")
pessoas = [
    {
        'nome': 'fulano',
        'idade': 19,
        'email': 'fulano@gmail.com',
        'profissao': 'Estudante'
    },
    {
        'nome': 'cicrano',
        'idade': 32,
        'email': 'cicrano@gmail.com',
        'profissao': 'DBA'
    },
    {
        'nome': 'deltrano',
        'idade': 25,
        'email': 'deltrano@gmail.com',
        'profissao': 'engenheiro'
    }
]

for pessoa in pessoas:
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}.")
print(f"\n{'-'*40}\n")

# novo dicionario

nova_pessoa = {
	'nome': "José",
	'idade': 20,
	'email': "jose@gmail.com",
	'profissão': "CEO"
}

# adicionando novo dicionario na lista

pessoas.append(nova_pessoa)

for pessoa in pessoas:
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}.")
print(f"\n{'-'*40}\n")


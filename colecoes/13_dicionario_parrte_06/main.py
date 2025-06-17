chaves = ('Nome', 'Idade', 'E-mail', 'Profissão')
pessoas = [
    {
        chaves[0]: "Bianca Cristina",
        chaves[1]: 20,
        chaves[2]: "bianca@gmail.com",
        chaves[3]: "CEO"
    },
    {
        chaves[0]: "Maria da Silva",
        chaves[1]: 25,
        chaves[2]: "maria@gmail.com",
        chaves[3]: "Assistente Administrativo"
    }
]

# Inserir novo dicionário
pessoa = {}

# Inserir dados no novo dicionário

try:
    for chave in chaves:
        if chave == 'Idade':
            pessoa[chave] = int(input(f"Informe Idade: "))
        else:
            pessoa[chave] = input(f"Informe {chave}: ")
    pessoas.append(pessoa)
    print(f"{pessoa.get(chave[0])} inserida com sucesso.")
except Exception as e:
    print(f"Não foi possível cadastrar nova pessoa. {e}.")
finally:
    for pessoa in pessoa:
        for chave in pessoa:
            print(f"{chave}: {pessoa.get(chave)}.")
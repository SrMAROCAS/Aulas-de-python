# Dicionário 
pessoa = {
    'nome': "Bianca Cristina", # nome é reconhecido como chave (nome da chave é uma string)
    'email': "biancacalopes@gmail.com",
}

# Exibindo os dados
print(f"Nome: {pessoa['nome']}")
print(f"Email: {pessoa.get('email')}")

# Exibir dados inexistentes
print(f"Idade: {pessoa.get('idade')}") # O get retorna None se a chave não existir

# Inserindo a idade da pessoa
try:
    pessoa['idade'] = int(input("Informe a idade: "))  
except Exception as e:
    print(f"não foi possíve inserir o novo valor. {e}.")
finally:
    print(f"Nome: {pessoa.get('nome')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"Idade: {pessoa.get('idade')}")
# Dicionário
usuario = {
    'nome' : "Fulano de Tal",
    'idade' : 18,
    'e-mail' : "fulano@gmail.com",
    'telefone' : "(61) 98765-4321",
    'profissão' : "Programador"
}

# O usuário escolhe a chave que deseja alterar
chave = input("Informe o nome da chave que desehja alterar: ").lower().strip()

try:
    if chave in usuario:
        usuario[chave] = input("Informe o novo valor: ")
        print(f"Chave {chave} alterada com sucesso!")
    else:
        print("Não foi possível encontrar a chave requisitada.")
except Exception as e:
    print(f"Não foi possível alterar. {e}.")
finally: 
    # Exibe os novos valores bo dicionário
    for chave in usuario:
        print(f"{chave.capitalize()} : {usuario.get(chave)}.")
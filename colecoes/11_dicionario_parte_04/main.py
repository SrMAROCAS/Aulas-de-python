# Dicionário
usuario = {
    'nome' : "Alex Machado",
    'idade' : 40,
    'e-mai' : "alex@gmail.com",
     'profissão' : "Programador"
}

# Usuário informa qual chave ele irá deletar
chave = input("Informe o nome da chave que deseja deletar: ").lower().strip()

#Tratamento de excessão
try:
    if chave in usuario:
        del usuario[chave]
    else:
        print("Não foi possível achar a chave")
except Exception as e:
    print(f"Não foi possível deletar a chave. {e}.") 
finally:
    # Exibe os valores do dicionário 
    for chave in usuario:
        print(f"{chave.capitalize()} : {usuario.get(chave)}.")
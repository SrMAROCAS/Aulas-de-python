from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
        nome ="",
        idade = 0,
        email = "",
        telefone = "",
        profissao = "",
        peso = 0.0,
        altura = 0.0  
        )
    
    usuario.nome = "João"
    usuario.idade = 30
    usuario.email = "jão@gmail.com"
    usuario.telefone = "123456789"
    usuario.profissao = "Engenheiro"
    usuario.peso = 75.5
    usuario.altura = 1.80
    print(f"{usuario}, tenho {len(usuario)} anos. Segue meus dados:\n")
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Profissão: {usuario.profissao}")
    print(f"Peso: {usuario.peso} kg")
    print(f"Altura: {usuario.altura} m")

    del(usuario)

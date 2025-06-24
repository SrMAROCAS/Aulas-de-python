# Class
# snakecase diferente de pascalcase (iniciar sempre em letra maíscula, se separação em caso de ser nome composto sendo a primeira letra da segunda pessoa maiúscula)
class Pessoa:
    # Atributos
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

# Algoritmo principal
if __name__ == "__main__":
    # Instancia a classe Pessoa (Cria objeto da classe)
    usuario = Pessoa()

    # Exibe na tela os dados do usuário
    print(f"Nome: {usuario.nome}.") 
    print(f"Idade: { usuario.idade}.")
    print(f"E-mail: {usuario.email}.")
    print(f"Profissão: {usuario.profissao}.")
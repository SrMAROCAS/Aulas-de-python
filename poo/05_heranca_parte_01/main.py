# bibliotecas
import classes
import os

#Algoritmo principal
if __name__ == "__main__":
    usuario = classes.PessoaFisica("", "", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")
    os.system("cls" if os.name == "nt" else "clear")

    # atributos valores ao objeto do tipo Pessoa Fisica
    print(f"{'_'*20} DADO DO USUÁRIO {'_'*20}\n")

    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.profissao = input("Informe sua profissao: ").strip()
    usuario.genero = input("Informe seu gênero: ").strip()
    usuario.email = input("Informe seu e-mail: ").lower().strip()
    usuario.endereco = input("Informe seu endereço: ").strip().title()
    usuario.telefone = input("Informe seu telefone: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    # atributos valores ao objeto do tipo Pessoa Jurídica
    print(f"{'_'*20} DADO DA EMPRESA {'_'*20}\n")
    
    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").title().strip()
    empresa.cnpj = input("Informe a CNPJ da empresa: ").strip()
    empresa.email = input("Informe o e-mail da empresa: ").lower().strip()
    empresa.endereco = input("Informe o endereço da empresa: ").title().strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    #Exibe osa dados do usuário e da empresa
    print("Dados do usuário:\n")
    usuario.exibir_dados()

    print('_'*60)
    print("Dados do da empresa:\n")
    empresa.exibir_dados()
#Importações
from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    #Instancia os objetos
    usuario = PessoaFisica(nome="", cpf="", profissao="", email="", telefone="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="")

    print(f"{'-'*20} Dados do Usuário {'-'*20}")
    usuario.nome = input("Informe o nome: ").title().strip()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.profissao = input("Informe a profissão: ").strip()
    usuario.email = input("Informe o e-mail: ").lower().strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    limpar()

    print(f"{'-'*20} Dados da Empresa {'-'*20}")
    empresa.razao_social = input("Informe a razão social: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").lower().strip()
    empresa.telefone = input("Informe o telefone: ").strip()

    limpar()
    print(f"{'-'*20} Dados do Usuário {'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Profissão: {usuario.profissao}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

    print(f"{'-'*20} Dados da Empresa {'-'*20}")
    print(f"Razão Social: {empresa.razao_social}")
    print(f"Nome Fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"E-mail: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")
    print(f"{'-'*57}" )

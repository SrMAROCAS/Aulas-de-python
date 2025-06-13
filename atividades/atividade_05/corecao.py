"""
Atividade -  Crie um programa que receba do usuário os seguintes dados:
- Nome
- CPF
- Data de Nascimento
- E-mail
- Genero
- Telefone
- Endereço
- Altura em metros
- Peso em kg
- Tipo sanguíneo
Ao final, o programa exibe esses dados
NOTE - deve ser feito utilizando dicionários
"""
import os
pessoa = { }
try:
    pessoa['nome'] = input("Infrome o nome: ")
    pessoa['cpf'] = (input("Infrome ou CPF: "))
    pessoa['data_nascimento'] = input("Infrome a data de nascimento (dd/mm/aaaa):")
    pessoa['e-mail'] = input("Infrome o e-mail: ")
    pessoa['genero'] = input("Infrome o gênero: ")
    pessoa['telefone'] = input("Infrome o telefone: ")
    pessoa['endereço'] = (input("Infrome o endereço: "))
    pessoa['altura'] = float(input("Infrome a altura (em metros): ").replace(',', '.'))
    pessoa['peso'] = float(input("Infrome seu peso (em quilos): ").replace(',', '.'))
    pessoa['tipo sangue'] = input("Infrome seu tipo sanguíneo: ")

    os.system("cls")

    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get[chave]}")

except Exception as e:
    print(f"Não foi possível rodar o programa. Erro: {e}")

''' 
# Tupla
campos = (
    "nome",
    "cpf",
    "data_nascimento",
    "email",
    "genero",
    "telefone",
    "endereco",
    "altura",
    "peso",
    "tipo_sanguineo"
)

pessoa = { }

for campo in campos:
    valor = input(f"Infrome seu {campo.replace('_', ' ')}: ")
    if campo in ["altura", "peso"]:
        valor = float(valor.replace(',', '.'))
    pessoa[campo] = valor
'''
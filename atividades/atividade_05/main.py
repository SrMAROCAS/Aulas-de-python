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

pessoa['nome'] = input("Infrome seu nome: ")
os.system("cls")
pessoa['cpf'] = (input("Infrome seu CPF: "))
os.system("cls")
pessoa['data_nascimento'] = input("Infrome sua data de nascimento (dd/mm/aaaa):")
os.system("cls")
pessoa['email'] = input("Infrome seu e-mail: ")
os.system("cls")
pessoa['genero'] = input("Infrome seu gênero: ")
os.system("cls")
pessoa['telefone'] = int(input("Infrome telefone: "))
os.system("cls")
pessoa['altura'] = float(input("Infrome sua altura (em metros): ").replace(',', '.'))
os.system("cls")
pessoa['peso'] = float(input("Infrome seu peso (em quilos): ").replace(',', '.'))
os.system("cls")
pessoa['tipo_sangue'] = input("Infrome seu tipo sanguíneo: ")
os.system("cls")

print(f"{'-'*15} Dados cadastrados {'-'*15}")
for dado in pessoa:
    print(f" {pessoa.get(dado)}")



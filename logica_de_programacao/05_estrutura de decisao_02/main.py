'''Crie um programa que recebe o nome, a idade e a altura do usuário, e verifique se o usuário tem a idade e a altura mínima para entrar
 no brinquedo. Caso não tenha, o programa deverá barra a entrada do usuário'''

#Declaração de variável
nome = input ("Informe o nome do usuário: ")
idade = int(input("Informe a idade do usuário: ")) 
altura = float(input("Informe a altura do usuário: ").replace(",", "."))

#Verifica a idade e a altura do usuário
if idade >= 12 and altura >= 1.10:
    print(f"A entrada de {nome} foi autorizada.")
else:
    print(f"A entrada de {nome} foi negada.")
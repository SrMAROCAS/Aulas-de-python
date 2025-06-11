''' 
Programa que irá receber do usuário dois números reais e o usuário irá escolher uma das quatros operações básicas da matemática, e o 
programa irá calcular com base na escolha do usuário e informar o resultado

    TODO
'''

#Declaração da variável
x = float(input("Informe o valor de x: ").replace(",", "."))
y = float(input("Informe o valor de y: ").replace(",", "."))

#Menu
print(f"{'-'*20} CALCULADORA PHYTON {'-'*20}") #O - aparecerá 20 vezez
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - divisão\n")

operador = input("informe a opção desejada: ")

#Verificar a operação escolhida e fazer o ccálculo
match operador: #Verifica se o usuário escolheu uma opção disposta pelo programa (substitui switch)
    case "1":
        print(f"O resultado da soma é: {x + y}.")
    case "2":
        print(f"O resultado da subtração é: {x - y}")
    case "3":
        print(f"O resultado da multiplicação é: {x * y}")
    case "4":
        print(f"O resultado da multiplicação é: {x / y}")
    case _:
        print("Operador inválido")
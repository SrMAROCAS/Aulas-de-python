'''Crie um programa que receba do usuário dois números reais, e uma das 4 operações da matemática informadas pelo usuário, e faça o cálculo
corespondente'''
    #NOTE

try:
    x = float(input("Informe o valor de x: ").replace(",", "."))
    y = float(input("Informe o valor de y: ").replace(",", "."))
    
    print(f"Qual ")
except Exception as e:
    print(f"Não foi possível possível ralizar a operação.  {e}.")
finally:
    print("Programa encerrado.")


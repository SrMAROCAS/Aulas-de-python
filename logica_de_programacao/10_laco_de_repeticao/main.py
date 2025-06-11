#Tratamento de exceção
try:
    #Declaração de variável
    n = int(input("Informe um número inteiro positivo"))

    #Laço de repetição
    while n>= 0:
        print(n)
        n -= 1
except Exception as e:
    print(f"Não foi posssível fazer a contagem. {e}.")
finally:
    print("Programa encerrado.")
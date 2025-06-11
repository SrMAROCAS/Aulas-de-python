#Tratamento de exceção
try:
    #Declaração de variável
    numero = int(input("informe um número inteiro: "))

    #Saída de dados
    print(f"O número informado é{numero}.")
except Exception as e:
    print(f"Não foi possível imprimir o número.  {e}.")
finally:
    print("Programa encerrado.")
    
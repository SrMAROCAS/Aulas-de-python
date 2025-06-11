# Declaração de variáveis 
nome = input("Informe seu nome: ")
'''idade = input("Informe sua idade:") ao invés de declarar dessa maneira (reconhece a variável como string) declare-a como: '''
idade = int(input("informe sua idade:"))
# Saída de dados
if idade >= 18:
    print(f"{nome} é maior de idade")
else: 
    print(f"{nome} é menor de idade")
#Declaração de variáveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

#Ternário (substitui o if eles, porém apenas em caso de estruturas pequenas)
result = "é maior de idade." if idade >= 18 else "é menor de idade."

#Saída de dados
print(f"{nome} {result}")
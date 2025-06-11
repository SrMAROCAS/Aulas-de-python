'''Programa que receba o nome e a média final de um aluno, e o programa retorna se o aluno foi aprovado, se ficou de resuperação, ou se
foi reprovado, com base em sua média final

    NOTE - A média deverá ser entre 0 e 10
    NOTE - Média para aprovação = 7. Reprovação 5.
'''

#Declaração de variáveis
nome = input("Informe o nome do aluno: ")
media = float(input("Informe a média do aluno: ").replace(",", ".")) #Comando .replace lê se o usuário tanto ,(virgula) em um float quanto . (ponto)

#Verifica se a média está dentro do intervalo
if media >= 0 and media <=10:
    if media<=7:
        print(f"{nome} está aprovado.")
    elif media >= 5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado")
else: 
    print("Valor da média inválida.")

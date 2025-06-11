''' Fazer um programa que verifica a partir de um laço de repetição, várias vezes, até o usuário parar de exceutar'''

#Laço de repetição
while True:
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    result = "É maior de idade." if idade >= 18 else "É menor de idade."
    
    print (f"{nome} {result}")

    repetir = input("Deseja verificar de novo? (s/n) ").lower() .strip()
    #.lower()Capta tanto maiúscula quanto minúscula
    #.strip() é para eliminar uma barra de espaço antes e depois de uma string

    match repetir:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção inválida")
            break
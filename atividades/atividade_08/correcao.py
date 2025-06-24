import os
import math as m

#Funções
def quadrado(l):
    a = l**2
    return a

def retangulo(b, h):
    a = b * h
    return a

def triangulo(b, h):
    a = (b*h)/2
    return a

def trapezio(B, b, h):
    a = ((B+h)*h)/2
    return a

while True:
    try:
        print("1 - Calcular área de um quadrado")
        print("2 - Calcular área de um retângulo")
        print("3 - Calcular área de um triangulo")
        print("4 - Calcular área de um trapézio")
        print("5 - Sair do programa...")
        opcao = input("Informe a operação desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case"1":
                l = float(input("Informe o valor do lado quadrado").raplace(",","."))
                os.system("cls" if os.name == "nt" else "clear")
                area = quadrado(1)
                print(f"A área do quadrado é {area}.")
                continue
            case"2":
                b = float(input("Informe o valor da base do retângulo: ").replace(",", "."))
                h = float(input("Informe a área da altura do retângulo: ").replace(",","."))
                os.system("cls" if os.name == "nt" else "clear")
                area = retangulo(b, h)
                print(f"A área de retângulo é {area}.")
                continue
            case"3":
                b = float(input("Informe o valor da base do triângulo: ").replace(",", "."))
                h = float(input("Informe a área da altura do triângulo: ").replace(",","."))
                os.system("cls" if os.name == "nt" else "clear")
                area = triangulo(b, h)
                print(f"A área de triângulo é {area}.")
                continue
            case"4":
                b = float(input("Informe o valor da base menor do trapézio: ").replace(",", "."))
                B = float(input("Informe o valor da base maior do trapézio: ").replace(",", "."))
                h = float(input("Informe a área da altura do trapézio: ").replace(",","."))
                os.system("cls" if os.name == "nt" else "clear")
                area = trapezio(B, b, h)
                print(f"A área de triângulo é {area}.")
                continue
            case"5":
                print("Programa encerrando")
                break
            case _:
                print("Opção inválida")
                continue
    except Exception as e:
        print (f"Não foi possível calcular. {e}.")
        continue
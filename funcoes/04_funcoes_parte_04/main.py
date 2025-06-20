import os
import math as m

# Funções
def mostrar_pi():
    return m.pi

def calcular_circunferencia(r):
    c = 2*m.pi*r
    return c

def calcular_area_circulo(r):
    a = m.pi*r**2
    return a

# Algoritmo principal
while True:
    print("1 - Mostrar número do pi")
    print("2 - Calcular tamanho da circunferência")
    print("3 - calcular área do círculo")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    try:
        if opcao == "2" or opcao == "3":
            r = float(input("Informar o valor do raio: ").replace(",", "."))
        else:
            ...
        match opcao:
            case "1":
               print(f"Número do pi: {mostrar_pi()}.")
               continue
            case "2":
                print(f"Tamanho da circunferência:{calcular_area_circulo(r)}")
                continue
            case "3":
                print(f"Área do circulo: {calcular_area_circulo(r)}")
                continue
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opções inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível executar cálculo. {e}.")
        continue
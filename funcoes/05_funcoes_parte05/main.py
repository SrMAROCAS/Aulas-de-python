# módulos - desenvolver a própria biblioteca
import os
import modulo

while True:
    try: 
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair do programa")
        opcao = input("Informe a operação deseja: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            x = float(input("Informe o valor de X: ").replace(",", "."))
            y = float(input("Informe o valoe de Y: ").replace(",", "."))

        else:
            ...
        match opcao:
            case "1":
                result = modulo.somar(x, y)
                print(f"O Valor da soma é {result}.")
                continue
            case "2":
                result = modulo.subtrair(x, y)
                print(f"O valor subtração é {result}.")
                continue
            case "3":
                result = modulo.multiplicar(x, y)
                print(f"O valor da Multiplicação é {result}.")
                continue
            case "4":
                result = modulo.dividir(x, y)
                print(f"O valor da divisão é {result}.")
                continue
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Operação inválida.")
                continue


    except Exception as e: 
        print("Não foi possível calcular. {e}.")
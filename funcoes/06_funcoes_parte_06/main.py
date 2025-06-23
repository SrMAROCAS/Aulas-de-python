'''
Crie um programa que calcule a questão do 1° grau.
- Coloque um menu para o ususário decidir se quer calcular a equação ou sair do programa.
- coloque no menu a opção de calcular a equação do 2° grau (não precisa desenvolver essa função por enquanto)
- Faça usando o conceito de módulo recém-ensinado, usando o comando 'import equacoes' no main. py.
'''
import os
import equacoes as eq

if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular equação de 1° grau.")
            print("2 - Calcular equação de 2° grau.")
            print("3 - Sair do programa.")
            opcao = input("Informe a operação desejada: ").strip()
            os.system("cls" if os.name == "nt" else "clear")

            match opcao:
                case "1":
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.primeiro_grau(a, b)
                    print(f"{a}x + {b} = 0" if b >= 0 else f"{a}x{b} = 0")
                    print(f"x = {result}")
                    continue 

                case "2":
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    c = float(input("Informe o valor de 'c': ").replace(",","."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.segundo_grau(a, b, c)
                    for x in result:
                        print(x)
                    continue

                case "3":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Operação inválida.")
                    continue
        except Exception as e: 
            print("Não foi possível calcular. {e}.")
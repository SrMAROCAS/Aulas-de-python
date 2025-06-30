from classes import Aluno, Curso
import os

def limpar():
        os.system("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    alunos = []
    cursos = []
    matricula = 0
    limpar()

    while True:
        aluno = Aluno(nome="", matricula=0, cpf="")
        curso = Curso(nome_curso="")
        print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}")
        print("1 - Cadastrar Aluno")
        print("2 - Cadastrar Curso")
        print("3 - Matricular aluno no Curso")
        print("4 - Listar Cursos")
        print("5 - Listar Alunos")
        print("6 - sair do programa")
        opcao = input("Digite a opção desejada: ").strip()

        limpar()
        match opcao:
            case "1":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do aluno: ").title().strip()
                    aluno.cpf = input("Informe o CPF do aluno: ").strip()
                    aluno.matricula = matricula
                    alunos.append(aluno)
                    limpar()

                    print(f"Aluno {aluno.nome} cadastrado com sucesso!")
                except Exception as e:
                    print(f"Não foi possível cadastrar aluno: {e}.")
                finally:
                    continue
            case "2":
                try:
                    
                    curso.nome_curso= input("Informe o curo: ").title().strip()
                    cursos.append(curso)
                    limpar()

                    print(f"Curso {curso.nome_curso} cadastrado com sucesso!")
                except Exception as e:
                    print(f"Não foi possível cadastrar curso: {e}.")
                finally:
                    continue
            case "3":
                try:
                    print(f"{'-'*10} Lista de Alunos {'-'*10}")
                    for aluno in alunos:
                        print(f"Nome: {aluno.nome}")
                        print(f"Matrícula: {aluno.matricula}")
                        print(f"CPF: {aluno.cpf}")
                        print(f"{'-'*37}")
                    inscricao = input("Digite a matrícula do aluno que deseja matricular: ").strip()
                    
                    for aluno in alunos:
                        aluno = {
                            'nome': aluno.nome,
                            'matricula': aluno.matricula,
                            'cpf': aluno.cpf
                        }
                        if inscricao in aluno['matricula']:
                            break
                        else:
                            ...
                    limpar()

                    print(f"{'-'*10} Lista de Cursos {'-'*10}")
                    for curso in cursos:
                        print(f"Curso: {curso.nome_curso}")
                        print(f"{'-'*37}")
                    curso_inscricao = input("Informe o curso desejado: ").title().strip()
                    aluno.inscrever_curso(curso_inscricao)
                    limpar()

                    print(f"Aluno {aluno.nome} inscrito no curso {curso.nome_curso} com sucesso!")
                    # else:
                    #     print("Não foi possível encontrar a matrícula.")
                except Exception as e:
                    print(f"Não foi possível matricular o aluno: no curso {e}.")
                finally:
                    continue
            case "4":
                cursos.nome_curso.sort()
                for curso in cursos:
                    print(f"Curso: {curso.nome_curso}")
                    print(f"Alunos:")
                    curso.listar_alunos().sort()
                    for aluno in curso.listar_alunos():
                        print(aluno)
                    print(f"{'-'*37}")
            case "5":
                alunos.nome.sort()
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")
                    print(f"Matrícula: {aluno.matricula}")
                    print(f"CPF: {aluno.cpf}")
                    print("Cursos matrículados:")
                    aluno.listar_cursos().sort()
                    for curso in aluno.listar_cursos():
                        print(curso)
                    print(f"{'-'*37}")

            case "6":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida.")
                continue

    # aluno01 = Aluno("Fulano", "101", "123.456.789-00")
    # aluno02 = Aluno("Ciclano", "102", "987.654.321-00")
    # aluno03 = Aluno("Beltrano", "103", "456.789.123-00")
    # aluno04 = Aluno("João", "104", "321.654.987-00")
    # aluno05 = Aluno("Maria", "105", "654.321.789-00")
    # aluno06 = Aluno("José", "106", "789.123.456-00")

    # #cursos
    # curso01 = Curso("Python Developer")
    # curso02 = Curso("IA com Python")
    # curso03 = Curso("Desenvolvedor Java")

    # #Inscrevendo alunos nos cursos
    # aluno01.increver_curso(curso01)
    # aluno02.increver_curso(curso01)
    # aluno03.increver_curso(curso01)

    # aluno04.increver_curso(curso02)
    # aluno05.increver_curso(curso02)

    # aluno06.increver_curso(curso03)

    # print(f"curso {curso01.nome_curso} tem os alunos: {curso01.listar_alunos()}")
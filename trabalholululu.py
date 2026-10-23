alunos = []


def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO ---")

    nome = input("Nome do aluno: ")
    turma = input("Turma do aluno: ")

    try:
        nota1 = float(input("Primeira nota: "))
        nota2 = float(input("Segunda nota: "))

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            print("As notas devem estar entre 0 e 10.")
            return

    except ValueError:
        print("Digite notas válidas.")
        return

    codigo = len(alunos) + 1

    aluno = {
        "codigo": codigo,
        "nome": nome,
        "turma": turma,
        "nota1": nota1,
        "nota2": nota2
    }

    alunos.append(aluno)

    print(f"Aluno cadastrado! Código: {codigo}")


def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            media = (aluno["nota1"] + aluno["nota2"]) / 2

            print("--------------------")
            print("Código:", aluno["codigo"])
            print("Nome:", aluno["nome"])
            print("Turma:", aluno["turma"])
            print("Média:", round(media, 2))


def pesquisar_aluno():
    print("\n--- PESQUISAR ALUNO ---")
    pesquisa = input("Digite o nome ou código do aluno: ")

    encontrado = False

    for aluno in alunos:
        if (pesquisa.lower() == aluno["nome"].lower()
                or pesquisa == str(aluno["codigo"])):

            print("Aluno encontrado!")
            print("Código:", aluno["codigo"])
            print("Nome:", aluno["nome"])
            print("Turma:", aluno["turma"])
            encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")


def calcular_media():
    print("\n--- CALCULAR MÉDIA ---")

    try:
        codigo = int(input("Digite o código do aluno: "))
    except ValueError:
        print("Digite um código válido.")
        return

    for aluno in alunos:
        if aluno["codigo"] == codigo:
            media = (aluno["nota1"] + aluno["nota2"]) / 2

            print("Aluno:", aluno["nome"])
            print("Média:", round(media, 2))

            if media >= 7:
                print("Situação: Aprovado")
            elif media >= 5:
                print("Situação: Recuperação")
            else:
                print("Situação: Reprovado")

            return

    print("Aluno não encontrado.")


def menu():
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Pesquisar aluno")
        print("4 - Calcular média e situação")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            pesquisar_aluno()
        elif opcao == "4":
            calcular_media()
        elif opcao == "5":
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
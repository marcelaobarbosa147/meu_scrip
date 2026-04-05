while True:
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "6":
        print("Encerrando a calculadora...")
        break

    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Opção inválida!")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except:
        print("Erro: digite apenas números!")
        continue

    if opcao == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcao == "4":
        if num2 == 0:
            print("Erro: divisão por zero!")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)

    elif opcao == "5":
        resultado = num1 ** num2
        print("Resultado:", resultado)

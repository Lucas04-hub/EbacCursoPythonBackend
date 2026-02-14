while True:
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisisão")

    opcao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", num1 + num2)
    elif opcao == "2":
        print("Resultado:", num1 - num2)
    elif opcao == "3":
        print("Resultado:", num1 * num2)
    elif opcao == "4":
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            print("Resultado:", num1 / num2)
    else:
        print("Operação inválida.")

continuar = input("Deseja realizar outra operação? Digite 's' para sim, e digite 'n' para não: ")

if continuar == 's':
    continuar = True
else:
    continuar = False
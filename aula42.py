

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("Error: Entrada invalida. Por favor, digite um numero")
except ZeroDivisionError:
    print("Não existe divisão por zero!")
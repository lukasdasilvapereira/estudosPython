
try:
    print("Bem vindo a calculadora de divisão")

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    result = n1 / n2

    print(result)
except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)    
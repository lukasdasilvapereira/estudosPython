print("Bemm vindo a melhor calculadora de Python")

n1 = float(input("Escolha o primeiro número: "))
n2 = float(input("Escolha o segundo número: "))

op1 = str(input("Escolha o operador: "))

if op1 == "+":
    print(n1 + n2)
elif op1 == "-":
     print(n1 - n2)
elif op1 == "/":
      print(n1 / n2)
elif op1 == "*":
      print(n1 * n2)
else:
      print("Escolha um operador de verdade")     
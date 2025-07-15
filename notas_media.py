n1 = float(input("Digite sua Primeira nota: "))
n2 = float(input("Digite sua Segunda nota: "))
n3 = float(input("Digite sua Terceira nota: "))

result = (n1 + n2 + n3) / 3
numero_menor = round(result,2)

print(f"A média é {numero_menor}")
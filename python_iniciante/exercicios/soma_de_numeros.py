n1 = int(input("Digite um número: "))
soma = 0

for index in range(1, n1 + 1):
    soma += index

print(f"A soma de 1 a {n1} é {soma}")
idade = int(input("Qual a sua idade?: "))

if idade >= 65:
    print(f"Sua idade é {idade}, Você já é idoso!")
elif idade >= 18:
    print(f"Sua idade é {idade}, Você é maior de idade!")
else:
    print(f"Sua idade é {idade}, Você não é maior de idade!")
print("Vamos contar as vogais")

n1 = input("Digite uma palavra: ")
contador = 0

for vowel in n1:
    if vowel.lower() in "aeiou":
        contador += 1
print(f"{n1} possui {contador} vogais")


lucky_numbers = [0 , 1 , 2 , 3, 4 , 5]
people = ["Lucas", "Bernardo", "Raquel"]

## people.extend(lucky_numbers) // VAI JUNTAR AS LISTAS
people.append("Creed")
people.insert(1, "Kelly")
people.remove("Creed")
##people.clear() // vai remover todos os elementos da lista
people.pop()
people.sort()
lucky_numbers.reverse()
print(lucky_numbers)
print(people)
print(people.index("Lucas"))
print(people.count("Lucas"))

friends2 = people.copy()

print(friends2)
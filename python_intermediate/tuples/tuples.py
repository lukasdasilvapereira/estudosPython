my_tuples = ("Max", 28, "Boston")

print(my_tuples)

my_list = ("Max",)

print(type(my_list))

print(my_tuples[0])
print(my_tuples[-1])

for i in my_tuples:
    print(i)


if "Max" in my_tuples:
    print("Yes")
else:
    print("No")


tuples = ("a", "p", "p", "l", "e")

print(tuples.count("p"))
print(tuples.index("a")) ## RETORNA ONDE A POSIÇÃO Q ESTÁ A LETRA

my_list = list(my_tuples) ## CONVERTE EM LISTA

print(my_list)

my_tuples2 = tuple(my_list) ## CONVERTE PRA TUPLES

## UNPACKING

mine_tuple = "Lucas", 19, "NI"

name, age, city = mine_tuple

print(city)

mine_tuple2 = 0, 1, 2 ,3 , 4 

i1, *i2, i3 = mine_tuple2

print(i2) ## AO COLOCAR A ESTRELA , ELE VAI MOSTRAR OS ITENS QUE NÃO FORAM DESEMPACOTADOS


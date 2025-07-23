## SETS: NÃO SÃO PERMITIDOS DUPLICATAS, LISTA MAS COM CHAVES, NÃO POSSUI ORDEM

myset = {1, 2, 3, 4 , 5}
print(myset)

my_list = set([5, 6, 7]) ## CONVERTER PARA SETS

print(my_list)

my_set = set() ## SET VAZIA

print(my_set)

my_set.add(1) ## ADICIONAR ITENS
my_set.add(2) ## ADICIONAR ITENS
my_set.remove(1) ## REMOVE
my_set.discard(2) ## OUTRO REMOVE

for i in myset:
    print(i)

if 1 in myset:
    print("Yes")
else:
    print("No")


uniao = my_set.union(myset) ## VAI COMBINAR OS ELEMENTOS

inter = myset.intersection(my_set) ## VAI VER QUAIS NUMEROS IGUAIS ELES POSSUEM

diferente = my_set.difference(myset) ## VAI CHECAR OS NÚMEROS DIFERENTES

myset.update(myset)  ## JUNTA OS DOIS, CRIANDO UM NOVO SET
myset.intersection_update(my_set) ## CRIA OUTRO SET , MAS APENAS COM OS ELEMENTOS IGUAIS DOS DOIS 
myset.difference_update(my_set) ## CRIA OUTRO SET MAS USANDO APENAS ELEMENTOS DIFERENTES


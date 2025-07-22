me = {"name": "Lucas", "age": 19, "city": "New York"}
outro = {"name":" Luan", "age": 9, "city": "London"}
print(me)

me = dict(me) ## VAI CONVERTER O ELEMENTO EM UM DICIONARIO

print(me["name"])

me["email"] = "lucaspereira021@gmail"  ## ADICIONA MAIS UM ELEMENTO

print(me)

me.pop("email") ## VAI DELETAR O ELEMENTO

if "age" in me:
    print(me["age"])


for key in me.values():
    print(key)

my_dict = me ## VAI COPIAR
my_dict = me.copy() ## PODE COPIAR ASSIM TBM

me.update(outro) ## UPDATE

print(me)


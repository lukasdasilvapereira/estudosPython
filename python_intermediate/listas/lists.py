mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist[0]

print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("Yes")
else:
    print("no")

## METHODS

print(len(mylist))

mylist.append("lemon")

print(mylist)

mylist.insert(1, "blueberry")

print(mylist)

mylist.pop()

mylist.remove("cherry")
mylist2.clear()
mylist.reverse()
mylist.sort()

a = mylist[0:2]
b = mylist[::1] ## VAI DO PRIMEIRO ATÉ O ULTIMO EM UM EM UM 

print(a)
print(b)

## COPY LIST

list_org = [1,2 ,3 ,4 ,5]

list_copy = list_org.copy()

print(list_copy)
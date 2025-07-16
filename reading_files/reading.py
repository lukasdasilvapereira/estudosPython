# open("url", r) => READ FILE
# open("url", w) => WRITE FILE
# open("url", a) => ADD ITEMS TO FILE
# open("url", r+) => READ AND WRITE FILE

employee_file = open("reading_files/employees.txt", "r")

print(employee_file.readable())
print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines())
#print(employee_file.readlines()[1])

employee_file.close()
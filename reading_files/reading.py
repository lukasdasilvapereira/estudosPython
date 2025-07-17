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

for employee in employee_file.readlines():
    print(employee)

employees = open("reading_files/employees.txt", "a") ## ADD TEXT TO THE FINAL

employees.write("\nToby - Human Resources")

employees.close()
    
employee_file.close()


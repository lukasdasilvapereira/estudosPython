print(2**3)

def exponent(n1, n2):
    result = 1
    for index in range(n2):
        result = result * n1
    return result 

print(exponent(3, 5))
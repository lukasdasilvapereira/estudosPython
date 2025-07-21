def verificar(name):
    if name.lower() == name[::-1]:
        return True
    else:
       return False

print(verificar("python"))
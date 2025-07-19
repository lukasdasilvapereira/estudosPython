class Car:
    def __init__(self, modelo, ano, vm, va, esta_ligado):
        self.modelo = modelo
        self.ano = ano
        self.vm = vm
        self.va = va
        self.esta_ligado = esta_ligado

corolla = Car("Corolla", 2020, 200, 0, False)

print(corolla)
print(corolla.modelo)


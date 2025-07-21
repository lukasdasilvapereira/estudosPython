class contaBancaria:
    def __init__(self, titular, saldo, depositar, sacar):
        self.titular = titular
        self.saldo = saldo
        self.depositar = depositar
        self.sacar = sacar
        

person1 = contaBancaria("Lucas", 1500, 1000, 500)

print(person1)
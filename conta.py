class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def get_numero(self):
        return self.numero
    def get_saldo(self):
        return self.saldo
    def debitar_saldo(self, valor):
        self.saldo -= valor
    def aplicar_saldo(self, valor):
        self.saldo += valor

conta1 = Conta(1234567890, 1000)
conta2 = Conta(1234567891, 2000)

def transferir(conta1, conta2, valor):
    conta1.debitar_saldo(valor)
    conta2.aplicar_saldo(valor)

transferir(conta1, conta2, 500)
print(conta1.get_saldo())
print(conta2.get_saldo())
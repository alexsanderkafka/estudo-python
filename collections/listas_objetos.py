class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_maria = ContaCorrente(15)
print(conta_maria)

conta_maria.deposita(500)
print(conta_maria)

conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)
print(conta_dani)

contas = [conta_maria, conta_dani]

print(contas)

for conta in contas:
    print(conta)

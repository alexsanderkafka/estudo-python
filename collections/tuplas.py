class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


conta_maria = ContaCorrente(15)
print(conta_maria)

conta_maria.deposita(500)
print(conta_maria)

conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)
print(conta_dani)

contas = [conta_maria, conta_dani]

print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

maria = ('Maria', 37, 1981)
dani = ('Dani', 31, 1987)

print(maria)
print(dani)

conta_maria = (15, 1000)


def deposita(conta):
    valor = conta[1] + 100
    codigo = conta[0]
    return (codigo, valor)


conta_maria = deposita(conta_maria)
print(conta_maria)

usuarios = [maria, dani]
print(usuarios)

usuarios.append(('Paulo', 39, 1979))
print(usuarios)

conta_maria = ContaCorrente(15)
conta_maria.deposita(500)
conta_dani = ContaCorrente(23)
conta_dani.deposita(1000)

contas = (conta_maria, conta_dani)
print(contas)

for conta in contas:
    print(conta)

contas[0].deposita(300)

for conta in contas:
    print(conta)

# consigo alterar valores de um objeto dentro de uma tupla
# cada posição da tupla tem um significado


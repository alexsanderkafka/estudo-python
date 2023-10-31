idades = [39, 30, 27, 18]

print(type(idades))

print(len(idades))

print(idades[0])
print(idades[1])
print(idades[2])
print(idades[3])

print(idades)

idades.append(90)
idades.append(2)

print(idades)

for idade in idades:
    print(idade)

idades.pop()

print(idades)

idades.remove(39)

print(idades)

if (15 in idades):
    idades.remove(15)
else:
    print("Não está em idades")

print(idades)

idades.append(19)

idades.insert(0, 20)

print(idades)

idades.extend([15, 90, 10, 90])

print(idades)

idades_next = []
for idade in idades:
    idades_next.append(idade+1)

print(idades_next)

idades_next = []

idades_next = [(idade + 1) for idade in idades]

print(idades_next)

idades_maior = [(idade) for idade in idades if idade > 21]

print(idades_maior)

idades_next = []


def proximo_ano(idade):
    return idade + 10


idades_next = [(proximo_ano(idade)) for idade in idades if idade > 21]

print(idades_next)

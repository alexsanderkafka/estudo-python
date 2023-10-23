arquivo = open("jogos/palavras.txt", "w")

print(arquivo)

"""
arquivo.write("banana\n")

arquivo.write("melancia")
"""

arquivo = open("jogos/palavras.txt", "a")

# arquivo.write("morango\n")

arquivo.write("maça\n")

arquivo.close()

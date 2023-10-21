def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")

    palavra_secreta = "banana".upper()

    enforcou = False
    acertou = False

    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    tentativa = 0

    while (not enforcou and not acertou):

        chute_user = input("Digite uma letra: ").upper().strip()

        index = 0

        if (chute_user in palavra_secreta):
            for letra in palavra_secreta:
                if (chute_user == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativa += 1

        enforcou = tentativa == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()

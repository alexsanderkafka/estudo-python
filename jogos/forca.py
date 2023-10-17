def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")

    palavra_secreta = "banhia".upper()

    enforcou = False
    acertou = False


    while (not enforcou and not acertou):

        chute_user = input("Digite uma letra: ").upper().strip()

        index = 0

        for letra in palavra_secreta:
            if (chute_user == letra):
                print("Encontrei a letra {} na posição {}".format(
                    chute_user, index))
            index += 1

        print("JOGANDO...")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()

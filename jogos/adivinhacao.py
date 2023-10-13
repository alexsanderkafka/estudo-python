import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    """
    while (rodada <= total_tentativas):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        numero_user = int(input("Digite um número: "))
        print("Você digitou ", numero_user)

        acertou = number_secret == numero_user
        maior = number_secret < numero_user
        menor = number_secret > numero_user

        if (acertou):
            print("Você acertou o número secreto")
            break
        elif (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

        rodada += 1
    """

    number_secret = random.randrange(1, 101)

    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for i in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(i, total_tentativas))

        numero_user = int(input("Digite um  entre 1 e 100: "))
        print("Você digitou ", numero_user)

        if (numero_user < 1 or numero_user > 100):
            print("Alert!!! Você deve digitar um número entre 1 e 100")
            continue

        acertou = number_secret == numero_user
        maior = number_secret < numero_user
        menor = number_secret > numero_user

        if (acertou):
            print("Você acertou o número secreto e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontos_perdidos = abs(number_secret - numero_user)
            pontos -= pontos_perdidos

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()

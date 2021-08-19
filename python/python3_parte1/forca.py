def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0
    # enquanto nao enforceou E nao acertou
    print(letras_acertadas)
    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    # print("Encontrei a letra {} na posição {}".format(chute,index))
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
    
    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar()

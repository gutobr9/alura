def jogar():

    palavra_secreta = "computador".strip().upper()
    palavra_mascara = []
    erros = 0
    acertos = 0
    # print(palavra_secreta)
    palavra_mascara = ["_" for letra in palavra_secreta]
    # print(palavra_mascara)

    while (("_" in palavra_mascara) and (erros < 6)):
        chute = input("Digite (sair) para finalizar o jogo | Digite qual a letra? ").strip().upper()
        if(chute == "SAIR"):
            break
        if(chute in palavra_mascara):
            print("Essa letra já existe!")
        else:
            if(len(chute) > 1):
                print("Digite apenas uma letra")
            else:
                index_palavra_mascara = 0
                if(chute in palavra_secreta):
                    for letra in palavra_secreta:
                        if(letra == chute):
                            palavra_mascara[index_palavra_mascara] = chute
                            acertos += 1
                        index_palavra_mascara += 1
                    print("Palavra secreta: {}".format(palavra_mascara))    
                else:
                    erros += 1
                    print(erros)
    print("Quant. acertos: {}".format(acertos))

if(__name__ == "__main__"):
    jogar()
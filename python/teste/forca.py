import random
def jogar():

    palavras = []

    arquivo = open("palavras.txt","r")
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    
    palavra_secreta = palavras[random.randrange(0,len(palavras))]
    palavra_mascara = []
    palavra_mascara = ["_" for letra in palavra_secreta]
    erros = 0

    while (("_" in palavra_mascara) and (erros < 6)):
        chute = input("Digite (sair) para finalizar o jogo | Digite qual a letra? ").strip().upper()
        if(chute == "SAIR"):
            print("------------------")
            print("Você saiu do jogo!")
            print("------------------")
            break
        elif(chute in palavra_mascara):
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
                        index_palavra_mascara += 1
                    print("Palavra secreta: {}".format(palavra_mascara))    
                else:
                    erros += 1
                    print("-------------")
                    print("Erros: {} de 6".format(erros))
                    print("-------------")
    if(chute != "SAIR"):
        print("-------------")
        if((not "_" in palavra_mascara)):
            print("VOCÊ GANHOU!!")
        else:
            print("Você perdeu!!")
        print("-------------")

if(__name__ == "__main__"):
    jogar()
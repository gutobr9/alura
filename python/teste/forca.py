import random
def jogar():

    imprimir_mensagem_abertura()
    
    palavra_secreta = gerar_palavra_secreta()
    
    palavra_mascara = inicializar_palavra_mascara(palavra_secreta)

    erros = 0

    while (("_" in palavra_mascara) and (erros < 6)):
        chute = chutar()
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


def imprimir_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def gerar_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    palavra_secreta = palavras[random.randrange(0,len(palavras))]
    return palavra_secreta

def inicializar_palavra_mascara(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def chutar():
    chute = input("Digite (sair) para finalizar o jogo | Digite qual a letra? ").strip().upper()
    return chute

if(__name__ == "__main__"):
    jogar()
# inteiros = [1,3,4,5,7,8,9]
# pares = []
# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(inteiros)
# print(pares)

# print("====================")

# List Comprehension
# pares = [i for i in inteiros if i % 2 == 0]
# impares = [i for i in inteiros if i % 2 != 0]

# print(inteiros)
# print("Pares: {}".format(pares))
# print("Ímpares: {}".format(impares))

# x = input("Digite: ")
# print(x)
# if(x == ""):
#     x = True
# print(type(x))

# palavra = "teste"

# t = ["_" for p in palavra]

# print(t)

# Leitura de arquivo
# arquivo = open("palavras.txt","w")
# limite = 11
# for x in range(1,limite):
#     if x == limite-1:
#         arquivo.write("teste {}".format(x)) 
#     else:
#         arquivo.write("teste {} \n".format(x)) 
# arquivo.close()

# Leitura apenas da primeira linha
# arquivo = open("palavras.txt","r")
# linha = arquivo.readline()
# print(linha)

# Leitura de palavras a partir de arquivo e escolhe randomica de uma palavra
# import random
# palavras = []
# arquivo = open("palavras.txt","r")
# for linha in arquivo:
#     palavras.append(linha.strip().upper())
# palavra_posicao = random.randrange(0,len(palavras))
# print(palavras)
# print(palavras[palavra_posicao])
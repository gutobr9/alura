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
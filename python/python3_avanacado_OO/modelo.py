class Filme:
    def __init__(self,nome,ano,duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao

    @property
    def nome(self):
        return self.__nome
    
    @property 
    def ano(self):
        return self.__ano
    
    @property
    def duracao(self):
        return self.__duracao

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano
    
    @duracao.setter
    def duracao(self,duracao):
        self.__duracao = duracao


class Serie:
    def __init__(self,nome,ano,temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def temporadas(self):
        return self.__temporadas

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano
    
    @temporadas.setter
    def temporadas(self,temporadas):
        self.__temporadas = temporadas

avengers = Filme("Avengers",2018,240)
# print(avengers)
# print(avengers.nome)
# avengers.nome = "vingadores"
# print(avengers.nome)
print(f"Filme: {avengers.nome} ano {avengers.ano} temporadas {avengers.duracao} minutos")
print("")
icarly = Serie("iCarly",2014,8)
# print("Série: {} ano {} temporadas {}".format(icarly.nome,icarly.ano,icarly.temporadas))
print(f"Série: {icarly.nome} ano {icarly.ano} temporadas {icarly.temporadas}")
# filme duracao
# serie temporadas

class Programa:
    def __init__(self,nome,ano):
        self.__nome = nome
        self.__ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self,ano):
        self.__ano = ano


class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        self.nome = nome
        self.ano = ano
        self.likes = 0
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self,duracao):
        self.__duracao = duracao

# p = Programa("Up",2005)

# for i in range(5):
#     p.dar_like()

# print(f"{p.nome} {p.ano} {p.likes}")

f = Filme("O Auto da Compadecida",1999,160)

for i in range(10):
    f.dar_like()

print(f"filme {f.nome} - ano {f.ano} - duracao {f.duracao} ")
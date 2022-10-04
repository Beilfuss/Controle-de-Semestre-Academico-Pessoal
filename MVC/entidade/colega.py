class Colega:

    def __init__(self, id: int, nome: str, matricula: str):
        
        if isinstance(id, int):
            self.__id = id

        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(matricula, str):
            self.__matricula = matricula
        


    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    def desempacotar(self):
        return {"nome": self.nome, "matricula": self.matricula}

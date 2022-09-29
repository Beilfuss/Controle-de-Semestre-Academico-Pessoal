class Colega:

    def __init__(self, nome: str, matricula: str):
        if isinstance(nome, str):
            self.__nome = nome
            self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    def desempacotar(self):
        return {"nome": self.nome, "matricula": self.matricula}

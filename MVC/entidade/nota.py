class Nota:

    def __init__(self, valor: int, peso: int):
        if isinstance(valor, int):
            self.__valor = valor
        if isinstance(peso, int):
            self.__peso = peso

    @property
    def valor(self):
        return self.__valor

    @property
    def peso(self):
        return self.__peso

    @valor.setter
    def valor(self, valor: int):
        if isinstance(valor, int):
            self.__valor = valor

    @peso.setter
    def peso(self, peso: int):
        if isinstance(peso, int):
            self.__peso = peso
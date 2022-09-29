class Colega:

    def __init__(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def nome(self):
        return self.__nome

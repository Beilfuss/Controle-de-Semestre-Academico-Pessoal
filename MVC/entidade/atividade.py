from entidade.nota import Nota


class Atividade:

    def __init__(self, nome: str, tipo: str, data: str, nota: Nota, grupo: bool, priorizar: bool):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(data, str):
            self.__data = data
        if isinstance(nota, Nota):
            self.__nota = nota
        if isinstance(grupo, bool):
            self.__grupo = grupo
        if isinstance(priorizar, bool):
            self.__priorizar = priorizar

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data(self):
        return self.__data

    @property
    def nota(self):
        return self.__nota

    @property
    def grupo(self):
        return self.__grupo

    @property
    def priorizar(self):
        return self.__priorizar

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo

    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data

    @nota.setter
    def nota(self, nota: Nota):
        if isinstance(nota, Nota):
            self.__nota = nota

    @grupo.setter
    def grupo(self, grupo: bool):
        if isinstance(grupo, bool):
            self.__grupo = grupo

    @priorizar.setter
    def priorizar(self, priorizar: bool):
        if isinstance(priorizar, bool):
            self.__priorizar = priorizar

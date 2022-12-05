from entidade.nota import Nota


class Atividade:

    def __init__(self, id: int, disciplina_id: int, nome: str, tipo: str, data: str, grupo: bool, priorizar: bool, pesoNota: int):
        if isinstance(id, int):
            self.__id = id
        if isinstance(disciplina_id, int):
            self.__disciplina_id = disciplina_id
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(data, str):
            self.__data = data
        if isinstance(pesoNota, int):
            self.__peso_nota = pesoNota
        if isinstance(grupo, bool):
            self.__grupo = grupo
        if isinstance(priorizar, bool):
            self.__priorizar = priorizar

    @property
    def id(self):
        return self.__id

    @property
    def disciplina_id(self):
        return self.__disciplina_id

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

    @property
    def peso_nota(self):
        return self.__peso_nota

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

    @peso_nota.setter
    def peso_nota(self, peso_nota: int):
        if isinstance(peso_nota, int):
            self.__peso_nota = peso_nota

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

    def desempacotar(self):
        return {
            "id": self.id,
            "disciplina_id": self.disciplina_id,
            "nome": self.nome,
            "tipo": self.tipo,
            "data": self.data,
            "peso_nota": self.peso_nota,
            "temGrupo": self.grupo,
            "priorizar": self.priorizar
        }

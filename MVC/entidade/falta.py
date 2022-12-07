

class Falta:

    def __init__(self, id: int, disciplina_id: int, dia: str, numFaltas: int):
        
        if isinstance(id, int):
            self.__id = id
        if isinstance(disciplina_id, int):
            self.__disciplina_id = disciplina_id
        if isinstance(dia, str):
            self.__dia = dia        
        if isinstance(numFaltas, int):
            self.__numFaltas = numFaltas

    @property
    def id(self):
        return self.__id

    @property
    def disciplina_id(self):
        return self.__disciplina_id

    @property
    def dia(self):
        return self.__dia

    @property
    def numFaltas(self):
        return self.__numFaltas

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id

    @disciplina_id.setter
    def disciplina_id(self, disciplina_id: int):
        if isinstance(disciplina_id, int):
            self.__disciplina_id = disciplina_id

    @dia.setter
    def dia(self, dia: str):
        if isinstance(dia, str):
            self.__dia = dia

    @numFaltas.setter
    def numFaltas(self, numFaltas: int):
        if isinstance(numFaltas, int):
            self.__numFaltas = numFaltas

    def desempacotar(self):

        return {
            "id": self.id,
            "disciplina_id": self.disciplina_id,
            "dia": self.dia,
            "numFaltas": self.numFaltas
        }
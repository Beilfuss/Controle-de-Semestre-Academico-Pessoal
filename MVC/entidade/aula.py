

class Aula:

    def __init__(self, id: int, dia: str, sala: str, horario: list):
        
        if isinstance(id, int):
            self.__id = id
        if isinstance(dia, str):
            self.__dia = dia        
        if isinstance(sala, str):
            self.__sala = sala
        if isinstance(horario, list):
            self.__horario = horario

    @property
    def id(self):
        return self.__id

    @property
    def dia(self):
        return self.__dia

    @property
    def sala(self):
        return self.__sala

    @property
    def horario(self):
        return self.__horario

    @dia.setter
    def dia(self, dia: str):
        if isinstance(dia, str):
            self.__dia = dia

    @sala.setter
    def sala(self, sala: str):
        if isinstance(sala, str):
            self.__sala = sala

    @horario.setter
    def horario(self, horario: list):
        if isinstance(horario, list):
            self.__horario = horario

    def adicionar_horario(self, horario: str):
        if isinstance(horario, str):
            self.__horario.append(horario)

    def remover_horario(self, horario: str):
        if isinstance(horario, str):
            for hora in self.__horario:
                if hora[0] == horario:
                    self.__horario.remove(hora)

    def desempacotar(self):

        return {
            "id": self.id,
            "dia": self.dia,
            "sala": self.sala,
            "horario": self.horario
        }
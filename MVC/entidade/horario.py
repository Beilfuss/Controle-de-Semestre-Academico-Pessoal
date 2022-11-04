

class Horario:
    
    def __init__(self, inicio: str, fim: str):


        if isinstance(inicio, str):
            self.__inicio = inicio        
        if isinstance(fim, str):
            self.__fim = fim

    @property
    def inicio(self):
        return self.__inicio

    @property
    def fim(self):
        return self.__fim

    @inicio.setter
    def inicio(self, inicio: str):
        if isinstance(inicio, str):
            self.__inicio = inicio

    @fim.setter
    def fim(self, fim: str):
        if isinstance(fim, str):
            self.__fim = fim

    def desempacotar(self):

        return {
            "inicio": self.inicio,
            "fim": self.fim
        }
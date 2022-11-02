class Grupo:

    def __init__(self):
        self.__numAlunos = 2
        self.__colegas = []

    @property
    def numAlunos(self):
        return self.__numAlunos

    @property
    def colegas(self):
        return self.__colegas

    @numAlunos.setter
    def numAlunos(self, num):
        if (isinstance(num, int)):
            self.__numAlunos = num

    def adicionar_colega(self, colega_id):
        if(isinstance(colega_id, int)):
            self.__colegas.append(colega_id)
    
    def remover_colega(self, colega_id):
        if colega_id in self.colegas:
            self.__colegas.pop(colega_id)
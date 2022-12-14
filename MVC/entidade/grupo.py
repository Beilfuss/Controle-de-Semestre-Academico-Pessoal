class Grupo:

    def __init__(self, id, numAlunos, colegas):

        if (isinstance(id, int)):
            self.__id = id

        if (isinstance(numAlunos, int)):
            self.__numAlunos = numAlunos

        if (isinstance(colegas, list)):
            self.__colegas = colegas

    @property
    def id(self):
        return self.__id

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

    def is_num_valido(self, num):
        return num > 1 and num >= len(self.colegas)

    def is_cheio(self):
        return len(self.colegas) >= self.numAlunos

    def is_membro(self, colega_id):
        return colega_id in self.colegas

    def adicionar_colega(self, colega_id):
        if (isinstance(colega_id, int)):
            self.__colegas.append(colega_id)

    def remover_colega(self, colega_id):
        if colega_id in self.colegas:
            self.__colegas.remove(colega_id)

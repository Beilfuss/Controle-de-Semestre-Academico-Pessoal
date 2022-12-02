
from dao.abstract_dao import AbstractDAO
from entidade.atividade import Atividade


class AtividadeDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.__load()

    def __load(self):
        return

    def create_table(self):
        
        return
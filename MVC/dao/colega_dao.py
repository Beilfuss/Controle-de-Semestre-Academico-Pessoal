
from dao.abstract_dao import AbstractDAO
from entidade.colega import Colega


class ColegaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.__load()

    def __load(self):
        query = "SELECT nome from colega"
        res = self.executar_query(query)
        for (nome,) in res:
            self._cache[nome] = Colega(nome)



    def create_table(self):

        query = "CREATE TABLE IF NOT EXISTS colega(nome TEXT UNIQUE)"
        self.executar_query(query)

    def persist_colega(self, nome):

        query = "INSERT INTO colega VALUES(?)"
        query_params = (nome,)

        try:
            self.executar_query(query, query_params)
            self._cache[nome] = Colega(nome)
            return True
        except Exception as err:
            print(err)
            return False

    def delete_colega(self, index):
        
        colega = list(self._cache.values())[index]
    

        query = "DELETE from colega where nome=(?)"
        query_params = (colega.nome,)
        self.executar_query(query, query_params)
        self._cache.pop(colega.nome)

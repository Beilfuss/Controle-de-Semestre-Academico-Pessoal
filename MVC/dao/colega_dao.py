
from dao.abstract_dao import AbstractDAO
from entidade.colega import Colega


class ColegaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.__load()

    def __load(self):

        # Obtém todos os dados salvos no banco e inicializa o cash instanciando os objetos correspondentes
        query = "SELECT nome, matricula from colega"
        res = self.executar_query(query)
        for (nome, matricula) in res:
            self._cache[matricula] = Colega(nome, matricula)

    def create_table(self):
        # Cria a tabela na primeira execução do programa
        query = "CREATE TABLE IF NOT EXISTS colega(nome TEXT, matricula TEXT UNIQUE)"
        self.executar_query(query)

    def persist_colega(self, nome, matricula):
        # Persiste um colega no banco de dados e instancia o objeto correspondente no cache
        query = "INSERT INTO colega VALUES(?, ?)"
        query_params = (nome, matricula)

        try:
            self.executar_query(query, query_params)
            self._cache[matricula] = Colega(nome, matricula)
            return True
        except Exception as err:
            return False

    def delete_colega(self, index):
        # deleta um colega do banco de dados e remove o objeto instanciado do cash

        colega = list(self._cache.values())[index]

        query = "DELETE from colega where matricula=(?)"
        query_params = (colega.matricula,)
        res = self.executar_query(query, query_params)

        self._cache.pop(colega.matricula)

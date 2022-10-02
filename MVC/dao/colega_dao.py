
# from readline import insert_text
from dao.abstract_dao import AbstractDAO
from entidade.colega import Colega


class ColegaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.__load()

    def __load(self):

        # Obtém todos os dados salvos no banco e inicializa o cash instanciando os objetos correspondentes
        query = "SELECT id, nome, matricula from COLEGAS"
        res = self.executar_query(query)
        for (id, nome, matricula) in res:
            print(id)
            self._cache[matricula] = Colega(id, nome, matricula)

    def create_table(self):
        # Cria a tabela na primeira execução do programa
        query = "CREATE TABLE IF NOT EXISTS COLEGAS(id INTEGER PRIMARY KEY ASC, matricula TEXT UNIQUE NOT NULL, nome TEXT NOT NULL)"
        self.executar_query(query)

    def obter_por_id(self, id):

        query = "SELECT id, nome, matricula FROM COLEGAS WHERE id=:id"
        query_params = {"id": id}

        colega = self.executar_query(query, query_params)[0]

        return colega

    def obter_por_matricula(self, matricula):

        return self.__cache[matricula]

    def persist_colega(self, nome, matricula):
        # Persiste um colega no banco de dados e instancia o objeto correspondente no cache
        query = "INSERT INTO COLEGAS(nome, matricula) VALUES(?, ?)"
        query_params = (nome, matricula)

        try:
            inserted_id = self.executar_query(query, query_params) #recebe o id do row inserido no banco

            (id, nome, matricula) = self.obter_por_id(inserted_id) #recebe os dados do objeto inserido no banco

            self._cache[matricula] = Colega(id, nome, matricula) #instancia o objeto  com os dados do banco
            return Colega
        except Exception as err:
            return False

    def delete_colega(self, index):
        # deleta um colega do banco de dados e remove o objeto instanciado do cash

        colega = list(self._cache.values())[index]

        query = "DELETE from COLEGAS where matricula=(?)"
        query_params = (colega.matricula,)
        res = self.executar_query(query, query_params)

        self._cache.pop(colega.matricula)

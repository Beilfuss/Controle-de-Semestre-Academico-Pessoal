
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
            self._cache[id] = Colega(id, nome, matricula)

    def create_table(self):
        # Cria a tabela na primeira execução do programa
        query = "CREATE TABLE IF NOT EXISTS COLEGAS(id INTEGER PRIMARY KEY ASC, matricula TEXT UNIQUE NOT NULL, nome TEXT NOT NULL)"
        self.executar_query(query)

    def obter_por_id(self, id):

        cached_colega = self._cache.get(id)
        if (cached_colega is not None):
            return cached_colega

        query = "SELECT id, nome, matricula FROM COLEGAS WHERE id=:id"
        query_params = {"id": id}

        colega = self.executar_query(query, query_params)[0]

        return colega

    def obter_por_matricula(self, matricula):

        colegas = list(filter(lambda colega: colega.matricula ==
                       matricula, self._cache.values()))

        colega = colegas[0] if len(colegas) != 0 else None

        return colega

    def persist_colega(self, nome, matricula):
        # Persiste um colega no banco de dados e instancia o objeto correspondente no cache
        query = "INSERT INTO COLEGAS(nome, matricula) VALUES(?, ?)"
        query_params = (nome, matricula)

        try:
            # recebe o id do row inserido no banco
            inserted_id = self.executar_query(query, query_params)

            # recebe os dados do objeto inserido no banco
            (id, nome, matricula) = self.obter_por_id(inserted_id)

            # instancia o objeto  com os dados do banco
            colega = Colega(id, nome, matricula)

            self._cache[id] = colega

            return colega
        except Exception as err:
            return False

    def alterar_colega(self, colega, nome):
        query = "UPDATE COLEGAS SET nome = ? WHERE id=?"
        query_params = (nome, colega.id)

        self.executar_query(query, query_params)

        colega.nome = nome

    def delete_colega(self, colega):
        # deleta um colega do banco de dados e remove o objeto instanciado do cash

        query = "DELETE from COLEGAS where id=(?)"
        query_params = (colega.id,)
        res = self.executar_query(query, query_params)

        self._cache.pop(colega.id)

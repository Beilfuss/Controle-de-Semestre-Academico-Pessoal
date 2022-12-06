from dao.abstract_dao import AbstractDAO
from entidade.grupo import Grupo


class GrupoDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.__load()

    def __load(self):

        # Obtém todos os dados salvos no banco e inicializa o cash instanciando os objetos correspondentes
        query = "SELECT id, numAlunos from GRUPOS"
        res = self.executar_query(query)
        for (group_id, numAlunos) in res:

            query = "SELECT colega_id FROM MEMBROS_GRUPO WHERE grupo_id=(?)"
            query_params = (group_id, )
            colegas = self.executar_query(query, query_params)

            colegas_ids = [colega_id for colega_id, in colegas]

            self._cache[group_id] = Grupo(group_id, numAlunos, colegas_ids)

    def create_table(self):
        # Cria as tabelas na primeira execução do programa
        query = "CREATE TABLE IF NOT EXISTS GRUPOS(id INTEGER PRIMARY KEY ASC, numAlunos INTEGER DEFAULT 2)"
        self.executar_query(query)

        query = "CREATE TABLE IF NOT EXISTS MEMBROS_GRUPO(grupo_id INTEGER NOT NULL, colega_id INTEGER NOT NULL, FOREIGN KEY(grupo_id) REFERENCES GRUPOS(id), FOREIGN KEY(colega_id) REFERENCES COLEGAS(id))"
        self.executar_query(query)

    def criar_grupo(self, atividade_id):
        query = "INSERT INTO GRUPOS(id, numAlunos) VALUES(?, 2)"
        query_params = (atividade_id,)

        inserted_id = self.executar_query(query, query_params)
        (id, numAlunos) = self.obter_por_id(inserted_id)

        grupo = Grupo(id, numAlunos, [])
        self._cache[id] = grupo
        return grupo

    def obter_por_id(self, id):

        cached_grupo = self._cache.get(id)
        if (cached_grupo is not None):
            return cached_grupo

        query = "SELECT id, numAlunos from GRUPOS WHERE id=:id"
        query_params = {"id": id}

        res = self.executar_query(query, query_params)

        return res[0] if len(res) > 0 else None

    def adiciona_membro(self, grupo, colega_id):

        query = "INSERT INTO MEMBROS_GRUPO(grupo_id, colega_id) VALUES(?,?)"
        query_params = (grupo.id, colega_id)

        self.executar_query(query, query_params)

        grupo.adicionar_colega(colega_id)

    def remover_membro(self, grupo, colega_id):

        query = "DELETE FROM MEMBROS_GRUPO WHERE colega_id=(?)"
        query_params = (colega_id,)

        self.executar_query(query, query_params)

        grupo.remover_colega(colega_id)

    def alterar_numero_colegas(self, grupo, numAlunos):

        query = "UPDATE GRUPOS SET numAlunos=(?) WHERE id=(?)"
        query_params = (numAlunos, grupo.id)

        self.executar_query(query, query_params)
        grupo.numAlunos = numAlunos

    def exists_grupo_anterior(self, colega_id, grupo_id):

        query = "SELECT EXISTS(SELECT * FROM MEMBROS_GRUPO WHERE grupo_id!=:grupo_id AND colega_id=:colega_id)"
        query_params = {"grupo_id": grupo_id,
                        "colega_id": colega_id}

        res = self.executar_query(query, query_params)
        exists = res[0][0]
        return exists == 1

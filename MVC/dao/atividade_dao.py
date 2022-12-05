
from dao.abstract_dao import AbstractDAO
from entidade.atividade import Atividade


class AtividadeDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.__load()

    def __load(self):
        query = "SELECT id, disciplina_id, nome, tipo, data, temGrupo, priorizar, peso_nota from ATIVIDADES"
        res = self.executar_query(query)
        for (id, disciplina_id, nome, tipo, data, temGrupo, priorizar, peso_nota) in res:
            self._cache[id] = Atividade(
                id, disciplina_id, nome, tipo, data, temGrupo != 0, priorizar != 0, peso_nota)

    def create_table(self):

        query = "CREATE TABLE IF NOT EXISTS ATIVIDADES(id INTEGER PRIMARY KEY ASC, disciplina_id INTEGER, nome TEXT NOT NULL, tipo TEXT NOT NULL, data TEXT NOT NULL, temGrupo INTEGER NOT NULL, priorizar INTEGER NOT NULL, peso_nota INTEGER NOT NULL, FOREIGN KEY(disciplina_id) REFERENCES DISCIPLINAS(id))																					"
        self.executar_query(query)

    def persist_atividade(self, disciplina_id, dados):

        # Persiste um colega no banco de dados e instancia o objeto correspondente no cache
        query = "INSERT INTO ATIVIDADES(disciplina_id, nome, tipo, data, temGrupo, priorizar, peso_nota) VALUES(?, ?, ?, ?, ?, ?, ?)"
        query_params = (disciplina_id, dados["nome"], "Prova" if dados[0] else "Trabalho",
                        dados["data"], dados["grupo"], dados["priorizar"], dados["peso"])

        try:
            # recebe o id do row inserido no banco
            inserted_id = self.executar_query(query, query_params)

            # recebe os dados do objeto inserido no banco
            (id, disciplina_id, nome, tipo, data, temGrupo,
             priorizar, peso_nota) = self.obter_por_id(inserted_id)

            # instancia o objeto  com os dados do banco
            atividade = Atividade(id, disciplina_id,
                                  nome, tipo, data, temGrupo != 0, priorizar != 0, peso_nota)

            self._cache[id] = atividade

            return atividade
        except Exception as err:
            return False

    def obter_por_id(self, id):

        cached_atividade = self._cache.get(id)
        if (cached_atividade is not None):
            return cached_atividade

        query = "SELECT id, disciplina_id, nome, tipo, data, temGrupo, priorizar, peso_nota from ATIVIDADES WHERE id=:id"
        query_params = {"id": id}

        atividade = self.executar_query(query, query_params)[0]

        return atividade

    def obter_por_disciplina(self, disciplina_id):

        atividades = list(filter(lambda atividade: atividade.disciplina_id ==
                                 disciplina_id, self._cache.values()))

        return atividades

    def priorizar(self, atividade):

        query = "UPDATE ATIVIDADES SET priorizar=:priorizar WHERE id=:id"
        query_params = {"priorizar": True, "id": atividade.id}

        self.executar_query(query, query_params)

        atividade.priorizar = True

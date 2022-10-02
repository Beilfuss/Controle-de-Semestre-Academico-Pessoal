from dao.abstract_dao import AbstractDAO
from entidade.disciplina import Disciplina


class DisciplinaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.__load()

    def __load(self):

        self.create_table()
        query = "SELECT nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas from DISCIPLINAS"
        res = self.executar_query(query)
        for (nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas) in res:
            self._cache[codigo] = Disciplina(nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas)

    def create_table(self):

        query = "CREATE TABLE IF NOT EXISTS DISCIPLINAS(id INTEGER PRIMARY KEY ASC, nome TEXT NOT NULL, codigo TEXT NOT NULL, professor TEXT NOT NULL, numAulas INTEGER NOT NULL, rec INTEGER NOT NULL, aulas NULL, faltas NULL, atividades NULL, colegas NULL)"
        self.executar_query(query)

    def persist_disciplina(self, nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas):

        query = "INSERT INTO DISCIPLINAS(nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        query_params = (nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas)

        try:
            self.executar_query(query, query_params)
            self._cache[codigo] = Disciplina(nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas)
            return True
        except Exception as err:
            print(err)
            return False

    def delete_disciplina(self, codigo):

        query = "DELETE from DISCIPLINAS where codigo=(?)"
        query_params = (codigo,)
        self.executar_query(query, query_params)

        self._cache.pop(codigo)
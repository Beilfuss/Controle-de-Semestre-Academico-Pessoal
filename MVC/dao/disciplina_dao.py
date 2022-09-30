from dao.abstract_dao import AbstractDAO
from entidade.disciplina import Disciplina


class DisciplinaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.__load()

    def __load(self):

        self.create_table()
        query = "SELECT codigo from disciplina"
        res = self.executar_query(query)
        for (codigo,) in res:
            self._cache[codigo] = Disciplina(codigo) # Aqui é só um atributo mesmo?

    def create_table(self):

        query = "CREATE TABLE IF NOT EXISTS disciplina(nome TEXT UNIQUE, codigo TEXT UNIQUE)"
        self.executar_query(query)

    def persist_disciplina(self, nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas):

        query = "INSERT INTO disciplina VALUES(?)"
        query_params = (nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas)

        try:
            self.executar_query(query, query_params)
            self._cache[codigo] = Disciplina(nome, codigo, professor, numAulas, rec, aulas, faltas, atividades, colegas)
            return True
        except Exception as err:
            print(err)
            return False

    def delete_disciplina(self, index):
        disciplina = list(self._cache.values())[index]

        query = "DELETE from disciplina where codigo=(?)"
        query_params = (disciplina.codigo,)
        self.executar_query(query, query_params)

        self._cache.pop(disciplina.codigo)
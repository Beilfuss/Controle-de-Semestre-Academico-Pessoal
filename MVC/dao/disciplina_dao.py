from dao.abstract_dao import AbstractDAO
from entidade.disciplina import Disciplina
from entidade.falta import Falta


class DisciplinaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.create_table_colegas_disciplinas()
        self.create_table_aulas_disciplinas()
        self.create_table_faltas()
        self.__cacheFaltas = []
        self.__load()

    def __load(self):

        query = "SELECT id, nome, codigo, professor, numAulas, rec, ativo from DISCIPLINAS"
        res = self.executar_query(query)
        for (id, nome, codigo, professor, numAulas, rec, ativo) in res:

            colegas = self.__obter_colegas(id)

            aulas = self.__obter_aulas(id)

            faltas = self.__obter_faltas(id)

            self._cache[id] = Disciplina(
                id, nome, codigo, professor, numAulas, rec, aulas, faltas, [], colegas, ativo)

    def __obter_colegas(self, id):

        query = "SELECT colega_id from COLEGAS_DISCIPLINAS WHERE disciplina_id=:id"
        query_params = {"id": id}

        res = self.executar_query(query, query_params)

        colegas = []
        for (id, ) in res:
            colegas.append(id)

        return colegas

    def __obter_aulas(self, id):
        
        query = "SELECT aula_id FROM AULAS_DISCIPLINAS WHERE disciplina_id=:id"
        query_params = {"id": id}

        res = self.executar_query(query, query_params)

        aulas = []
        for (id, ) in res:
            aulas.append(id)

        return aulas

    def __obter_faltas(self, id):
        
        query = "SELECT * FROM FALTAS WHERE disciplina_id=:id"
        query_params = {"id": id}

        res = self.executar_query(query, query_params)

        faltas = []
        for (id, disciplina_id, dia, numFaltas) in res:
            faltas.append(Falta(id, disciplina_id, dia, numFaltas))

        for f in faltas:
            self.__cacheFaltas.append(f)

        return faltas

    def create_table(self):
        # aulas, faltas, atividades e colegas não serão colunas da tabela disciplina
        query = "CREATE TABLE IF NOT EXISTS DISCIPLINAS(id INTEGER PRIMARY KEY ASC, nome TEXT NOT NULL, codigo TEXT NOT NULL, professor TEXT NOT NULL, numAulas INTEGER NOT NULL, rec INTEGER NOT NULL, ativo TEXT NOT NULL)"
        self.executar_query(query)

    def create_table_colegas_disciplinas(self):

        query = "CREATE TABLE IF NOT EXISTS COLEGAS_DISCIPLINAS(disciplina_id INTEGER NOT NULL, colega_id INTEGER NOT NULL, FOREIGN KEY(disciplina_id) REFERENCES DISCIPLINAS(id), FOREIGN KEY(colega_id) REFERENCES COLEGAS(id))"
        self.executar_query(query)

    def create_table_aulas_disciplinas(self):

        query = "CREATE TABLE IF NOT EXISTS AULAS_DISCIPLINAS(disciplina_id INTEGER NOT NULL, aula_id INTEGER NOT NULL, FOREIGN KEY(disciplina_id) REFERENCES DISCIPLINAS(id), FOREIGN KEY(aula_id) REFERENCES AULAS(id))"
        self.executar_query(query)

    def create_table_faltas(self):

        query = "CREATE TABLE IF NOT EXISTS FALTAS(id INTEGER PRIMARY KEY ASC, disciplina_id INTEGER NOT NULL, dia TEXT NOT NULL, numFaltas INTEGER NOT NULL, FOREIGN KEY(disciplina_id) REFERENCES DISCIPLINAS(id))"
        self.executar_query(query)

    def persist_faltas(self, dados_faltas):
        query = "INSERT INTO FALTAS(disciplina_id, dia, numFaltas) VALUES(?, ?, ?)"
        query_params = (dados_faltas["disciplina_id"], dados_faltas["dia"], dados_faltas["numFaltas"])

        try:

            inserted_id = self.executar_query(query, query_params)

            (id, disciplina_id, dia, numAulas) = self.obter_faltas_por_id(inserted_id)

            falta = Falta(id, disciplina_id, dia, numAulas)

            self.__cacheFaltas.append(falta)

            faltas = []
            for f in self.__cacheFaltas:
                if f.disciplina_id == dados_faltas["disciplina_id"]:
                    faltas.append(f)

            self._cache[disciplina_id].faltas = faltas

            return True
        
        except Exception as err:

            return False
        
    def delete_falta(self, id, disciplina_id):
        
        query = "DELETE from FALTAS where id=(?)"
        query_params = (id,)
        self.executar_query(query, query_params)

        disciplina_cached = self._cache.get(disciplina_id)
        disciplina_cached.remover_falta(id)

        for f in self.__cacheFaltas:
            if f.id == id:
                self.__cacheFaltas.remove(f)

    def obter_faltas_por_id(self, id):

        '''disciplina_cached = self._cache.get(id)
        if (disciplina_cached):
            return disciplina_cached.faltas'''
        
        query = "SELECT * FROM FALTAS WHERE id=:id"
        query_params = {"id": id}

        faltas_dados = self.executar_query(query, query_params)[0]

        return faltas_dados

    def obter_por_id(self, id):

        disciplina_cached = self._cache.get(id)
        if (disciplina_cached):
            return disciplina_cached

        query = "SELECT * FROM DISCIPLINAS WHERE id=:id"
        query_params = {"id": id}

        disciplina_dados = self.executar_query(query, query_params)[0]

        return disciplina_dados

    def persist_disciplina(self, dados_disciplina):

        query = "INSERT INTO DISCIPLINAS(nome, codigo, professor, numAulas, rec, ativo) VALUES(?, ?, ?, ?, ?, ?)"
        query_params = (dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                        dados_disciplina["numAulas"], dados_disciplina["rec"], "Sim")

        try:
            # adequações para utilizar o id como chave e os dados persistidos na instanciação do objeto disciplina. Garante consistência entre a memória e o banco.
            # recebe o id do row inserido no banco
            inserted_id = self.executar_query(query, query_params)

            (id, nome, codigo, professor, numAulas, rec, ativo) = self.obter_por_id(
                inserted_id)  # recebe os dados do objeto inserido no banco

            self._cache[id] = Disciplina(
                id, nome, codigo, professor, numAulas, rec, [], [], [], [], ativo)
            return True
            
        except Exception as err:

            return False

    def alterar_disciplina(self, dados_disciplina):
        query = "UPDATE DISCIPLINAS SET nome = ?, codigo = ?, professor = ?, numAulas = ?, rec = ? WHERE id = ?"
        query_params = (dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                        dados_disciplina["numAulas"], dados_disciplina["rec"], dados_disciplina['id'])
        self.executar_query(query, query_params)

        disciplina = self._cache[dados_disciplina['id']]

        disciplina.nome = dados_disciplina['nome']
        disciplina.codigo = dados_disciplina['codigo']
        disciplina.professor = dados_disciplina['professor']
        disciplina.numAulas = dados_disciplina['numAulas']
        disciplina.rec = dados_disciplina['rec']

    def delete_disciplina(self, id):

        disciplina = self.obter_por_id(id)

        query = "DELETE from DISCIPLINAS where id=(?)"
        query_params = (id,)
        self.executar_query(query, query_params)

        self._cache.pop(id)

        self.remover_colegas(id)

        if disciplina.aulas != []:
            id_aulas_para_excluir = self.remover_aulas(id)

            return id_aulas_para_excluir

    def encerrar_disciplina(self, id):
        query = "UPDATE DISCIPLINAS SET ativo = ? WHERE id = ?"
        query_params = ("Não", id)
        self.executar_query(query, query_params)

        disciplina = self._cache[id]
        disciplina.ativo = "Não"

    def incluir_colega(self, disciplina, colega):

        try:
            query = "INSERT INTO COLEGAS_DISCIPLINAS(disciplina_id, colega_id) VALUES(?, ?)"
            query_params = (disciplina.id, colega.id)

            self.executar_query(query, query_params)

            disciplina.adicionar_colega(colega.id)

            return True

        except Exception as err:
            return False

    def remover_colega(self, disciplina, colega):

        try:
            query = "DELETE FROM COLEGAS_DISCIPLINAS where disciplina_id=(?) and colega_id=(?)"
            query_params = (disciplina.id, colega.id)
            self.executar_query(query, query_params)

            

            disciplina.remover_colega(colega.id)

            return True

        except Exception as err:
            return False

    def remover_colegas(self, disciplina_id):

        query = "DELETE FROM COLEGAS_DISCIPLINAS where disciplina_id=(?)"
        query_params = (disciplina_id, )

        self.executar_query(query, query_params)

    def remover_aulas(self, disciplina_id):

        query = "SELECT aula_id FROM AULAS_DISCIPLINAS where disciplina_id=(?)"
        query_params = (disciplina_id, )
        id_aulas_para_excluir = self.executar_query(query, query_params)

        for aula in id_aulas_para_excluir:
            query = "DELETE FROM HORARIOS where id=(?)"
            query_params = aula
            self.executar_query(query, query_params)

            query = "DELETE FROM AULAS where id=(?)"
            query_params = aula
            self.executar_query(query, query_params)

        query = "DELETE FROM AULAS_DISCIPLINAS where disciplina_id=(?)"
        query_params = (disciplina_id, )
        self.executar_query(query, query_params)

        return id_aulas_para_excluir
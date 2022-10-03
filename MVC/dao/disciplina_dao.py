from dao.abstract_dao import AbstractDAO
from entidade.disciplina import Disciplina


class DisciplinaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.create_table_colegas_disciplinas()
        self.__load()

    def __load(self):
        
        #Alterei para buscar o id e utilizá-lo como chave em vez do código, conforme conversamos no whatsapp
        query = "SELECT id, nome, codigo, professor, numAulas, rec from DISCIPLINAS"
        res = self.executar_query(query)
        for (id, nome, codigo, professor, numAulas, rec) in res:

            colegas = self.__obter_colegas(id)

            self._cache[id] = Disciplina(id, nome, codigo, professor, numAulas, rec, [], [], [], colegas)


    def __obter_colegas(self,id):

        query = "SELECT colega_id from COLEGAS_DISCIPLINAS WHERE disciplina_id=:id"
        query_params = {"id": id}

        res = self.executar_query(query, query_params)

        colegas = []
        for (id, ) in res:
            colegas.append(id)

        return colegas

    def create_table(self):
        #aulas, faltas, atividades e colegas não serão colunas da tabela disciplina, conforme documento do sheets. Retirei da query. Adequei nos outros métodos
        query = "CREATE TABLE IF NOT EXISTS DISCIPLINAS(id INTEGER PRIMARY KEY ASC, nome TEXT NOT NULL, codigo TEXT NOT NULL, professor TEXT NOT NULL, numAulas INTEGER NOT NULL, rec INTEGER NOT NULL)"
        self.executar_query(query)

    def create_table_colegas_disciplinas(self):

        query= "CREATE TABLE IF NOT EXISTS COLEGAS_DISCIPLINAS(disciplina_id INTEGER NOT NULL, colega_id INTEGER NOT NULL, FOREIGN KEY(disciplina_id) REFERENCES DISCIPLINAS(id), FOREIGN KEY(colega_id) REFERENCES COLEGAS(id))"
        self.executar_query(query)


    def obter_por_id(self, id):

        disciplina_cached = self._cache.get(id)
        if(disciplina_cached):
            return disciplina_cached

        query = "SELECT * FROM DISCIPLINAS WHERE id=:id"
        query_params = {"id": id}

        disciplina_dados = self.executar_query(query, query_params)[0]

        return disciplina_dados


    def persist_disciplina(self, dados_disciplina):
        #Muitos argumentos, chamada fica estranha. Não seria melhor passar apenas um argumento (ex: dicionário contendo todos os dados) e utilizar os atributos do dicionário dentro do método?

        query = "INSERT INTO DISCIPLINAS(nome, codigo, professor, numAulas, rec) VALUES(?, ?, ?, ?, ?)"
        query_params = (dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                                        dados_disciplina["numAulas"], dados_disciplina["rec"])

        try:
            #adequações para utilizar o id como chave e os dados persistidos na instanciação do objeto disciplina. Garante consistência entre a memória e o banco.
            inserted_id = self.executar_query(query, query_params) #recebe o id do row inserido no banco
            
            (id, nome, codigo, professor, numAulas, rec) = self.obter_por_id(inserted_id) #recebe os dados do objeto inserido no banco
            
            self._cache[id] = Disciplina(id, nome, codigo, professor, numAulas, rec, [], [], [], [])
            return True
        except Exception as err:
           
            return False

    def alterar_disciplina(self, dados_disciplina):
        query = "UPDATE DISCIPLINAS SET nome = ?, codigo = ?, professor = ?, numAulas = ?, rec = ? WHERE id = ?"
        query_params = (dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                                        dados_disciplina["numAulas"], dados_disciplina["rec"], dados_disciplina['id'])
        self.executar_query(query, query_params)

        self._cache[dados_disciplina['id']].nome = dados_disciplina['nome']
        self._cache[dados_disciplina['id']].codigo = dados_disciplina['codigo']
        self._cache[dados_disciplina['id']].professor = dados_disciplina['professor']
        self._cache[dados_disciplina['id']].numAulas = dados_disciplina['numAulas']
        self._cache[dados_disciplina['id']].rec = dados_disciplina['rec']

    def delete_disciplina(self, id):
        #adequação para usar id no lugar de código
        query = "DELETE from DISCIPLINAS where id=(?)"
        query_params = (id,)
        self.executar_query(query, query_params)

        self._cache.pop(id)

    
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
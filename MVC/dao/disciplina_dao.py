from dao.abstract_dao import AbstractDAO
from entidade.disciplina import Disciplina


class DisciplinaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.__load()

    def __load(self):

        self.create_table()
        #Alterei para buscar o id e utilizá-lo como chave em vez do código, conforme conversamos no whatsapp
        query = "SELECT id, nome, codigo, professor, numAulas, rec from DISCIPLINAS"
        res = self.executar_query(query)
        for (id, nome, codigo, professor, numAulas, rec) in res:
            self._cache[id] = Disciplina(id, nome, codigo, professor, numAulas, rec, None, None, None, None)

    def create_table(self):
        #aulas, faltas, atividades e colegas não serão colunas da tabela disciplina, conforme documento do sheets. Retirei da query. Adequei nos outros métodos
        query = "CREATE TABLE IF NOT EXISTS DISCIPLINAS(id INTEGER PRIMARY KEY ASC, nome TEXT NOT NULL, codigo TEXT NOT NULL, professor TEXT NOT NULL, numAulas INTEGER NOT NULL, rec INTEGER NOT NULL)"
        self.executar_query(query)

    def obter_por_id(self, id):

        query = "SELECT * FROM DISCIPLINAS WHERE id=:id"
        query_params = {"id": id}

        disciplina_dados = self.executar_query(query, query_params)[0]

        return disciplina_dados


    def persist_disciplina(self, nome, codigo, professor, numAulas, rec):
        #Muitos argumentos, chamada fica estranha. Não seria melhor passar apenas um argumento (ex: discionário contendo todos os dados) e utilizar os atributos do dicionário dentro do método?

        query = "INSERT INTO DISCIPLINAS(nome, codigo, professor, numAulas, rec) VALUES(?, ?, ?, ?, ?)"
        query_params = (nome, codigo, professor, numAulas, rec)

        try:
            #adequações para utilizar o id como chave e os dados persistidos na instanciação do objeto disciplina. Garante consistência entre a memória e o banco.
            inserted_id = self.executar_query(query, query_params) #recebe o id do row inserido no banco
            
            (id, nome, codigo, professor, numAulas, rec) = self.obter_por_id(inserted_id) #recebe os dados do objeto inserido no banco
            
            self._cache[id] = Disciplina(id, nome, codigo, professor, numAulas, rec, None, None, None, None)
            return True
        except Exception as err:
            print(err)
            return False

    def delete_disciplina(self, id):
        #adequação para usar id no lugar de código
        query = "DELETE from DISCIPLINAS where id=(?)"
        query_params = (id,)
        self.executar_query(query, query_params)

        self._cache.pop(id)
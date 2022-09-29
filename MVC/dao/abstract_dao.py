from abc import ABC, abstractmethod
import sqlite3


class AbstractDAO(ABC):

    @abstractmethod
    def __init__(self, ):
        self.__db = "gerenciador.db"  # nome banco de dados
        self._cache = {}  # Atributo protegido

    def conectar(self):
        # conecta ao banco de dados
        return sqlite3.connect(self.__db)

    def buscar_todos(self):
        # retorna todos os objetos do cache em uma lista
        return list(self._cache.values())

    def executar_query(self, query, query_params=None):
        # executa a query informada, utilizando os parâmetros se existentes
        con = self.conectar()
        cur = con.cursor()

        
        res = cur.execute(query, query_params).fetchall(
        ) if query_params else cur.execute(query).fetchall()

        con.commit()
        con.close()

        return res

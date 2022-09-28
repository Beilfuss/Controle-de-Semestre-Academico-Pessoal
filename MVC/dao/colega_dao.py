import sqlite3
from entidade.colega import Colega


class ColegaDAO():

    def __init__(self):
        self.__db = "gerenciador.db"
        self.__cache = []
        self.__load()

    def __load(self):
        con = self.connect()
        cur = con.cursor()
        res = cur.execute("SELECT nome from colega").fetchall()
        con.close()

        self.__cache = [Colega(colega[0]) for colega in res]

    def get_all(self):
        return self.__cache

    def connect(self):
        return sqlite3.connect(self.__db)

    def close_connection(self, con):
        con.close()

    def create_table(self):

        con = self.connect()
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS colega(nome TEXT UNIQUE)")
        con.close()

    def persist_colega(self, nome):

        con = self.connect()
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO colega VALUES(?)", (nome,))
            con.commit()
            con.close()
            self.__cache.append(Colega(nome))
            return True
        except Exception as err:
            return False

    def delete_colega(self, index):
        colega = self.__cache[index]

        con = self.connect()
        cur = con.cursor()
        res = cur.execute("DELETE from colega where nome=(?)", (colega.nome,))
        con.commit()
        del self.__cache[index]
        con.close()

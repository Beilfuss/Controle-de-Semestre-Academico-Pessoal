from entidade.colega import Colega
from entidade.falta import Falta


class Disciplina:

    def __init__(self, id: int, nome: str, codigo: str, professor: str, numAulas: int, rec: str, aulas: list,
                 faltas: list, atividades: list, colegas: list, ativo: str):
        
        
        if isinstance(id, int):
            self.__id = id        
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, str):
            self.__codigo = codigo
        if isinstance(professor, str):
            self.__professor = professor
        if isinstance(numAulas, int):
            self.__numAulas = numAulas
        if isinstance(rec, str):
            self.__rec = rec
        if isinstance(aulas, list):
            self.__aulas = aulas
        if isinstance(faltas, list):
            self.__faltas = faltas
        if isinstance(atividades, list):
            self.__atividades = atividades
        if isinstance(colegas, list):
            self.__colegas = colegas
        if isinstance(ativo, str):
            self.__ativo = ativo

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def professor(self):
        return self.__professor

    @property
    def numAulas(self):
        return self.__numAulas

    @property
    def rec(self):
        return self.__rec

    @property
    def aulas(self):
        return self.__aulas

    @property
    def faltas(self):
        return self.__faltas

    @property
    def atividades(self):
        return self.__atividades

    @property
    def colegas(self):
        return self.__colegas

    @property
    def ativo(self):
        return self.__ativo

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @codigo.setter
    def codigo(self, codigo: str):
        if isinstance(codigo, str):
            self.__codigo = codigo

    @professor.setter
    def professor(self, professor: str):
        if isinstance(professor, str):
            self.__professor = professor

    @numAulas.setter
    def numAulas(self, numAulas: int):
        if isinstance(numAulas, int):
            self.__numAulas = numAulas

    @rec.setter
    def rec(self, rec: str):
        if isinstance(rec, str):
            self.__rec = rec

    @aulas.setter
    def aulas(self, aulas: list):
        if isinstance(aulas, list):
            self.__aulas = aulas

    @faltas.setter
    def faltas(self, faltas: list):
        if isinstance(faltas, list):
            self.__faltas = faltas

    @atividades.setter
    def atividades(self, atividades: list):
        if isinstance(atividades, list):
            self.__atividades = atividades

    @ativo.setter
    def ativo(self, ativo: str):
        if isinstance(ativo, str):
            self.__ativo = ativo

    def adicionar_colega(self, colega: int):
        if isinstance(colega, int):
            self.__colegas.append(colega)

    def remover_colega(self, colega: int):
        if isinstance(colega, int):
            self.__colegas.remove(colega)

    def adicionar_aula(self, aula: int):
        if isinstance(aula, int):
            self.__aulas.append(aula)

    def remover_aula(self, aula: int):
        if isinstance(aula, int):
            self.__aulas.remove(aula)     
    
    def remover_falta(self, id: int):
        if isinstance(id, int):
            for f in self.__faltas:
                if f.id == id:
                    self.__faltas.remove(f)

    def desempacotar(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "codigo": self.codigo,
            "professor": self.professor,
            "numAulas": self.numAulas,
            "rec": self.rec,
            "aulas": self.aulas,
            "faltas": self.faltas,
            "colegas": self.colegas,
            "ativo": self.ativo
        }

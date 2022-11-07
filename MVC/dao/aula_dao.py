from dao.abstract_dao import AbstractDAO
from entidade.aula import Aula


class AulaDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

        self.create_table()
        self.create_table_horarios()
        self.__load()

    def __load(self):

        query = "SELECT id, dia, sala from AULAS"
        res = self.executar_query(query)
        for (id, dia, sala) in res:

            horarios = self.obter_horarios_de_uma_aula(id)

            self._cache[id] = Aula(id, dia, sala, horarios)

    '''
    def __obter_horarios(self, id):
        
        query = "SELECT horario from HORARIOS WHERE id=:id"
        query_params = {"id": id}

        res = self.executar_query(query, query_params)

        horarios = []
        for (id, ) in res:
            horarios.append(id)

        return horarios
    '''

    def create_table(self):

        query = "CREATE TABLE IF NOT EXISTS AULAS(id INTEGER PRIMARY KEY ASC, dia TEXT NOT NULL, sala TEXT NOT NULL)"
        self.executar_query(query)

    def create_table_horarios(self):

        query = "CREATE TABLE IF NOT EXISTS HORARIOS(id INTEGER NOT NULL, horario TEXT NOT NULL, FOREIGN KEY(id) REFERENCES AULAS(id))"
        self.executar_query(query)

    def obter_por_id(self, id):

        aula_cached = self._cache.get(id)
        if (aula_cached):
            return aula_cached
        
        query = "SELECT * FROM AULAS WHERE id=:id"
        query_params = {"id": id}

        aula_dados = self.executar_query(query, query_params)[0]

        return aula_dados
    
    def obter_horarios_de_uma_aula(self, id):

        query = "SELECT horario FROM HORARIOS WHERE id=:id"
        query_params = {"id": id}

        todos_horarios = self.executar_query(query, query_params)

        return todos_horarios

    def verificar_dia_horario(self, dia, horario):

        aulas = self._cache
        aula_dia_horario_igual = None
        aulas_no_dia = []

        for aula in aulas:
            if aulas[aula].dia == dia:
                aulas_no_dia.append(aulas[aula])

        horarios_no_dia = []

        for j in range(len(aulas_no_dia)):
            for k in range(len(aulas_no_dia[j].horario)):
                horarios_no_dia.append(aulas_no_dia[j].horario[k][0])

        for hora in horarios_no_dia:
            if hora in horario:
                aula_dia_horario_igual = True

        return aula_dia_horario_igual

    def persist_aulas(self, dados_aula):

        query = "INSERT INTO AULAS(dia, sala) VALUES(?, ?)"
        query_params = (dados_aula["dia"], dados_aula["sala"])

        try:
            
            inserted_id = self.executar_query(query, query_params)

            (id, dia, sala) = self.obter_por_id(inserted_id)

            todos_horarios = self.persist_horarios(inserted_id, dados_aula['horarios'])
            
            aula = Aula(id, dia, sala, todos_horarios)

            self._cache[id] = aula

            return aula
        
        except Exception as err:

            return False
    
    def persist_horarios(self, inserted_id, horarios):

        for horario in horarios:
            
            query = "INSERT INTO HORARIOS(id, horario) VALUES(?, ?)"
            query_params = (inserted_id, horario)

            try:

                self.executar_query(query, query_params)

            except Exception as err:

                return False
        
        todos_horarios = self.obter_horarios_de_uma_aula(inserted_id)

        return todos_horarios
    
    def delete_aula(self, disciplina, aula_selecionada):
        
        aulas = self._cache

        for aula in aulas:
            if aulas[aula].dia == aula_selecionada[0]:
                if aulas[aula].sala == aula_selecionada[2]:
                    for tupla_horario in aulas[aula].horario:
                        if tupla_horario[0] == aula_selecionada[1]:
                            aula_obj = aulas[aula]
                            
        self.remover_horario(aula_obj, aula_selecionada[1])

        if aula_obj.horario == []:

            self.remover_aula(disciplina, aula_obj)

            query = "DELETE FROM AULAS WHERE id=(?)"
            query_params = (aula_obj.id,)

            self.executar_query(query, query_params)

            self._cache.pop(aula_obj.id)                        
    
    def update_aula(self, aula_antiga, dados_aula):

        horarios = self.obter_horarios_de_uma_aula(aula_antiga.id)

        query = "UPDATE AULAS SET sala = ?, dia = ? where id = ?"
        query_params = (dados_aula['sala'], dados_aula['dia'], aula_antiga.id)
        self.executar_query(query, query_params)

        for i in range(len(dados_aula['horarios'])):
            query = "UPDATE HORARIOS SET horario = ? where id = ? and horario = ?"
            query_params = (dados_aula['horarios'][i], aula_antiga.id, horarios[i][0])
            self.executar_query(query, query_params)

        horarios = self.obter_horarios_de_uma_aula(aula_antiga.id)
        
        aula_antiga.sala = dados_aula['sala']
        aula_antiga.dia = dados_aula['dia']
        print('aula_antiga.horarios ANTES: ', aula_antiga.horario)
        aula_antiga.horario = horarios
        print('aula_antiga.horarios DEPOIS: ', aula_antiga.horario)
        
    def remover_horario(self, aula, horario):

        try:
            query = "DELETE FROM HORARIOS WHERE id=(?) and horario=(?)"
            query_params = (aula.id, horario)

            self.executar_query(query, query_params)

            aula.remover_horario(horario)

            return True
        
        except Exception as err:
            return False
        
    def incluir_aula(self, disciplina, aula):

        try:
            query = "INSERT INTO AULAS_DISCIPLINAS(disciplina_id, aula_id) VALUES(?, ?)"
            query_params = (disciplina.id, aula.id)

            self.executar_query(query, query_params)

            disciplina.adicionar_aula(aula.id)

            return True
        
        except Exception as err:
            return False
        
    def remover_aula(self, disciplina, aula):

        try:
            query = "DELETE FROM AULAS_DISCIPLINAS where disciplina_id=(?) and aula_id=(?)"
            query_params = (disciplina.id, aula.id)

            self.executar_query(query, query_params)

            disciplina.remover_aula(aula.id)

            return True
        
        except Exception as err:
            return False

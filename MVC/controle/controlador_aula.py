from limite.tela_dados_aula import TelaDadosAula
from entidade.aula import Aula
from dao.aula_dao import AulaDAO
from excecoes.jaExistenteException import JaExistenteException

class ControladorAula:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela_dados_aula = TelaDadosAula(self)
        self.__dao = AulaDAO()

    def gerir_aulas(self, disciplina, aula_selecionada, opcao):
        opcoes = {'Cadastrar Aula': self.cadastrar_aula,
                  'Alterar Aula': self.alterar_aula,
                  'Excluir Aula': self.excluir_aula,
                  'Obter Aulas': self.obter_aulas_de_disciplina
                  }
        
        if opcao == 'Obter Aulas':
            return opcoes[opcao](disciplina)
        elif opcao == 'Excluir Aula' or opcao == 'Alterar Aula':
            opcoes[opcao](disciplina, aula_selecionada)
        else:
            opcoes[opcao](disciplina)

    def cadastrar_aula(self, disciplina):

        horarios = []
        dados_aula = {"sala": "", "dia": "", "horarios": "", "alteracao": False}
        
        while True:

            botao, dados_tela = self.__tela_dados_aula.abrir(dados_aula)

            self.__tela_dados_aula.fechar()

            if botao == "Cancelar":
                break

            elif botao == 'Adicionar Horário':
                dados_aula, horarios = self.adicionar_horario(dados_tela, dados_aula, horarios)

            elif botao == 'Excluir Horário':
                dados_aula, dados_tela = self.excluir_horario(dados_aula, dados_tela)

            elif botao == 'Cadastrar Aula':
                dados_aula['sala'] = dados_tela['sala']
                aula, horarios = self.validar_aula(dados_aula, horarios)
                
                if aula == None and horarios != []:
                    aula = self.__dao.persist_aulas(dados_aula)
                    self.__dao.incluir_aula(disciplina, aula)

                    return aula            

    def adicionar_horario(self, dados_tela, dados_aula, horarios):
        try:


            if (dados_tela['Segunda-feira'] == False and dados_tela['Segunda-feira'] == False and dados_tela['Terça-feira'] == False and dados_tela['Quarta-feira'] == False and dados_tela['Quinta-feira'] == False and dados_tela['Sexta-feira'] == False and dados_tela['Sábado'] == False) or dados_tela['horario'] == "":
                raise ValueError
            
            if dados_tela['sala'] == "" or dados_tela['sala'].isalpha() or dados_tela['sala'].isdigit():
                raise ValueError
            
            for horario in dados_aula['horarios']:
                if horario == dados_tela['horario']:
                    raise JaExistenteException
            
            condicoes = [dados_tela['Segunda-feira'], dados_tela['Segunda-feira'], dados_tela['Terça-feira'], dados_tela['Quarta-feira'], dados_tela['Quinta-feira'], dados_tela['Sexta-feira'], dados_tela['Sábado']]
            dias = ['Segunda-feira', 'Segunda-feira', 'Terça-feira','Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
            dia_semana = None
            i = 0
            for condicao in condicoes:
                if condicao == True:
                    dia_semana = dias[i]
                i += 1

            horarios.append(dados_tela['horario'])
                
            dados_aula = {"sala": dados_tela["sala"], "dia": dia_semana, "horarios": horarios, "alteracao": False}
            
            return dados_aula, horarios

        except ValueError:
            self.__tela_dados_aula.mostrar_mensagem("Atenção", "Dados inválidos. Tente novamente!")
            return dados_aula, horarios

        except JaExistenteException:
            self.__tela_dados_aula.mostrar_mensagem("Atenção", "Este horário já foi adicionado!")
            return dados_aula, horarios

    def excluir_horario(self, dados_aula, dados_tela):
        try:
            
            if dados_tela['row_index'] == []:
                raise ValueError

            del dados_aula['horarios'][dados_tela['row_index'][0]]

            return dados_aula, dados_aula

        except ValueError:
            self.__tela_dados_aula.mostrar_mensagem("Atenção", "Nenhum horário selecionado para ser excluído ou não há horários a serem selecionados!")
            return dados_aula, dados_aula
    
    def validar_aula(self, dados_aula, horarios):

        try:
             
            if dados_aula['sala'] == "" or dados_aula['dia'] == "" or dados_aula['horarios'] == "":
                raise ValueError
            
            if dados_aula['sala'] == "" or dados_aula['sala'].isalpha() or dados_aula['sala'].isdigit():
                raise ValueError

            aula = self.__dao.verificar_dia_horario(dados_aula["dia"], dados_aula["horarios"])

            if aula is not None:
                if dados_aula['alteracao'] == False:
                    dados_aula['dia'] = ""
                    dados_aula['sala'] = ""
                    dados_aula['horarios'] = []
                    horarios = []
                raise JaExistenteException
            
            if aula is None:
                return aula, horarios
            
        except JaExistenteException:
            self.__tela_dados_aula.mostrar_mensagem("Atenção!", "Já há aula cadastrada nesse dia e horário!")
            if dados_aula['alteracao'] == False:
                aula = None
                # horarios = None
            return aula, horarios
        except ValueError:
            self.__tela_dados_aula.mostrar_mensagem("Atenção!", "Dados inválidos. Tente novamente!")
            if dados_aula['alteracao'] == True:
                aula = False
            elif dados_aula['alteracao'] == False:
                aula = None
                horarios = []
            return aula, horarios
    
    def excluir_aula(self, disciplina, aula_selecionada):
        self.__dao.delete_aula(disciplina, aula_selecionada)

    def alterar_aula(self, disciplina, aula_selecionada):

        aulas = self.__dao._cache

        for aula in aulas:
            if aulas[aula].dia == aula_selecionada[0]:
                if aulas[aula].sala == aula_selecionada[2]:
                    for tupla_horario in aulas[aula].horario:
                        if tupla_horario[0] == aula_selecionada[1]:
                            aula_obj = aulas[aula]

        horarios = []

        for horario in aula_obj.horario:
            horarios.append(horario[0])

        dados_aula = {"sala": aula_obj.sala, "dia": aula_obj.dia, "horarios": horarios, "alteracao": True}

        while True:

            botao, dados_tela = self.__tela_dados_aula.abrir(dados_aula)

            self.__tela_dados_aula.fechar()
            
            if botao == "Cancelar":
                break

            elif botao == 'Adicionar Horário':
                dados_aula, horarios = self.adicionar_horario(dados_tela, dados_aula, horarios)

            elif botao == 'Excluir Horário':
                dados_aula, dados_tela = self.excluir_horario(dados_aula, dados_tela)

            elif botao == 'Cadastrar Aula':
                
                condicoes = [dados_tela['Segunda-feira'], dados_tela['Segunda-feira'], dados_tela['Terça-feira'], dados_tela['Quarta-feira'], dados_tela['Quinta-feira'], dados_tela['Sexta-feira'], dados_tela['Sábado']]
                dias = ['Segunda-feira', 'Segunda-feira', 'Terça-feira','Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
                dia_semana = None
                i = 0
                for condicao in condicoes:
                    if condicao == True:
                        dia_semana = dias[i]
                    i += 1

                if dados_aula['sala'] != dados_tela['sala'] and dados_tela['horario'] == '' and dados_aula['dia'] == dia_semana:
                    dados_aula['sala'] = dados_tela['sala']
                    self.__dao.update_aula(aula_obj, dados_aula)

                    return aula

                nome_sala_antigo = dados_aula['sala']
                dados_aula['sala'] = dados_tela['sala']
                    
                dados_aula['dia'] = dia_semana

                aula, horarios = self.validar_aula(dados_aula, horarios)

                if aula == False:
                    dados_aula['sala'] = nome_sala_antigo

                if dados_aula['horarios'] != [] and horarios != [] and aula == None:

                    self.__dao.update_aula(aula_obj, dados_aula)

                    return aula
    
    def obter_aulas_de_disciplina(self, disciplina):

        dict_aulas = self.__dao._cache

        aulas_de_disciplina = []

        for aula in dict_aulas:
            if dict_aulas[aula].id in disciplina.aulas:
                aulas_de_disciplina.append(dict_aulas[aula])

        dicts_aulas_de_disciplina = []
                
        for aula in aulas_de_disciplina:
            dicts_aulas_de_disciplina.append(aula.desempacotar())

        return dicts_aulas_de_disciplina
    
    def remover_aulas_cache(self, id_aulas_para_excluir):
        for id in id_aulas_para_excluir:
            self.__dao._cache.pop(id[0])
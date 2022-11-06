from limite.tela_dados_aula import TelaDadosAula
from entidade.aula import Aula
from dao.aula_dao import AulaDAO
from excecoes.jaExistenteException import JaExistenteException

class ControladorAula:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela_dados_aula = TelaDadosAula(self)
        self.__dao = AulaDAO()

    def cadastrar_aula(self, disciplina):

        horarios = []
        dados_aula = {"sala": "", "dia": "", "horarios": ""}
        
        while True:

            botao, dados_tela = self.__tela_dados_aula.abrir(dados_aula)

            self.__tela_dados_aula.fechar()

            if botao == "Cancelar":
                break

            elif botao == 'Adicionar Horário':
                try:

                    # Adicionar mais verificações
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
                        
                    dados_aula = {"sala": dados_tela["sala"], "dia": dia_semana, "horarios": horarios}
                    
                except ValueError:
                    self.__tela_dados_aula.mostrar_mensagem("Atenção", "Dados inválidos. Tente novamente!")
                except JaExistenteException:
                    self.__tela_dados_aula.mostrar_mensagem("Atenção", "Este horário já foi adicionado!")

            elif botao == 'Excluir Horário':

                try:
                    
                    if dados_tela['row_index'] == []:
                        raise ValueError

                    del dados_aula['horarios'][dados_tela['row_index'][0]]

                except ValueError:
                    self.__tela_dados_aula.mostrar_mensagem("Atenção", "Nenhum horário selecionado para ser excluído ou não há horários a serem selecionados!")

            elif botao == 'Cadastrar Aula':

                try:

                    if dados_aula['sala'] == "" or dados_aula['dia'] == "" or dados_aula['horarios'] == []:
                        raise ValueError

                    aula = self.__dao.verificar_dia_horario(dados_aula["dia"], dados_aula["horarios"])

                    if aula is not None:
                        dados_aula['horarios'] = []
                        horarios = []
                        raise JaExistenteException
                    
                    if aula is None:
                        aula = self.__dao.persist_aulas(dados_aula)
                        self.__dao.incluir_aula(disciplina, aula)

                    return aula
                
                except JaExistenteException:
                    self.__tela_dados_aula.mostrar_mensagem("Atenção!", "Já há aula cadastrada nesse dia e horário!")
                except ValueError:
                    self.__tela_dados_aula.mostrar_mensagem("Atenção!", "Algum campo ficou vazio ou nenhum horário foi adicionado!")

    def excluir_aula(self):
        pass        

    def obter_aulas_de_disciplina(self, disciplina):

        dict_aulas = self.__dao._cache
        
        aulas_de_disciplina = []

        for i in range(len(dict_aulas)):
            if dict_aulas[i+1].id in disciplina.aulas:
                aulas_de_disciplina.append(dict_aulas[i+1])

        dicts_aulas_de_disciplina = []
                
        for aula in aulas_de_disciplina:
            dicts_aulas_de_disciplina.append(aula.desempacotar())

        return dicts_aulas_de_disciplina
from limite.tela_dados_aula import TelaDadosAula
from entidade.aula import Aula
# from dao.aula_dao import AulaDAO
from random import randrange

class ControladorAula:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela_dados_aula = TelaDadosAula(self)
        # self.__dao = AulaDAO()
        '''self.__horarios_possiveis = ['07:30 - 08:20', '08:20 - 09:10', '09:10 - 10:10', '10:10 - 11:00', '11:00 - 11:50',
                                     '13:30 - 14:20', '14:20 - 15:10', '15:10 - 16:20', '16:20 - 17:10', '17:10 - 18:00',
                                     '18:30 - 19:20', '19:20 - 20:20', '20:20 - 21:10', '21:10 - 22:00']'''


    def cadastrar_aula(self, disciplina):

        horarios = []
        dados_aula = {"sala": "", "dia": "", "horarios": ""}
        
        while True:

            botao, dados_tela = self.__tela_dados_aula.abrir(dados_aula)
            
            print('botao: ', botao, 'dados_aula: ', dados_tela)

            self.__tela_dados_aula.fechar()

            if botao == "Cancelar":
                break

            elif botao == 'Adicionar Horário':
                try:

                    # Adicionar mais verificações
                    if (dados_tela['Segunda-feira'] == False and dados_tela['Segunda-feira'] == False and dados_tela['Terça-feira'] == False and dados_tela['Quarta-feira'] == False and dados_tela['Quinta-feira'] == False and dados_tela['Sexta-feira'] == False and dados_tela['Sábado'] == False) or dados_tela['horario'] == "":
                        raise ValueError
                    
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

            elif botao == 'Cadastrar Aula':
                pass

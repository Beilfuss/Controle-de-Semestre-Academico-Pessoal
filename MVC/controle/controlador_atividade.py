from limite.tela_atividade import TelaAtividade
from dao.atividade_dao import AtividadeDAO


class ControladorAtividade:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaAtividade(self)
        self.__dao = AtividadeDAO()

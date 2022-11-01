from limite.tela_grupo import TelaGrupo
from dao.grupo_dao import GrupoDao

class ControladorGrupo:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaGrupo(self)
        self.__dao = ColegaDAO()
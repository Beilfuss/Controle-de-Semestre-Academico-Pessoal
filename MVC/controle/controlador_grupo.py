from limite.tela_grupo import TelaGrupo
from dao.grupo_dao import GrupoDAO


class ControladorGrupo:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaGrupo(self)
        self.__dao = GrupoDAO()

    def inicializar(self, id_disciplina=1, nome_disciplina="Placeholder", id_atividade=1):

        # obter colegas - id - atividade
        # obter dados do grupo id - disciplina

        opcoes = {0: ""}

        opcao_escolhida, dados = self.__tela.abrir(nome_disciplina)

        if (opcao_escolhida != 0):
            return (opcao_escolhida, opcoes[opcao_escolhida](dados))
        else:
            return (opcao_escolhida, None)

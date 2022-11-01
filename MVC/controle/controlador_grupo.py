from limite.tela_grupo import TelaGrupo
from dao.grupo_dao import GrupoDAO


class ControladorGrupo:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaGrupo(self)
        self.__dao = GrupoDAO()

    def cadastrar_grupo(self, disciplina, atividade_id):

        # obter colegas - id - atividade
        # obter dados do grupo id - disciplina

        opcoes = {0: "", 1: lambda dados: self.adicionar_colega(),
                  2: lambda dados: self.excluir_colega(), 3: lambda dados: self.confirmar_cadastro()}

        while(True):
            opcao_escolhida, dados = self.__tela.abrir(disciplina.nome)

            if (opcao_escolhida != 0):
                opcao_escolhida, opcoes[opcao_escolhida](dados)
            else:
                return (opcao_escolhida, None)

    def adicionar_colega(self):

        print("A implementar")

    def excluir_colega(self):

        print("A implementar")

    def confirmar_cadastro(self):

        print("A implementar")

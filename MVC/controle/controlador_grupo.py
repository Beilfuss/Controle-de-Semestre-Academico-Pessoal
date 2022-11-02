from limite.tela_grupo import TelaGrupo
from dao.grupo_dao import GrupoDAO
from entidade.grupo import Grupo


class ControladorGrupo:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaGrupo(self)
        self.__dao = GrupoDAO()
        self.__grupos = []

    def cadastrar_grupo(self, disciplina_id, disciplina_nome, atividade_id):

        colegas = self.obter_colegas(disciplina_id)
        colegas_dados = [(colega.nome, colega.matricula) for colega in colegas]
        # obter dados do grupo id - disciplina

        opcoes = {0: "", 1: lambda dados: self.adicionar_colega(grupo, colegas, dados),
                  2: lambda dados: self.excluir_colega(), 3: lambda dados: self.confirmar_cadastro()}

        while (True):
            opcao_escolhida, dados = self.__tela.abrir(
                disciplina_nome, colegas_dados)

            if (opcao_escolhida != 0):
                opcao_escolhida, opcoes[opcao_escolhida](dados)
            else:
                return (opcao_escolhida, None)

    def obter_colegas(self, disciplina_id):
        # obter colegas - id - atividade
        return self.__controlador_sistema.obter_colegas_por_disc(disciplina_id)

    def adicionar_colega(self, grupo, colegas, dados):
        index = dados["novo_colega_index"][0]
        colega = colegas[index]

        # Verifica se o colega já está no grupo
        # Inclui o colega no grupo (ou não)

        print(index)

    def excluir_colega(self):

        print("A implementar")

    def confirmar_cadastro(self):

        print("A implementar")

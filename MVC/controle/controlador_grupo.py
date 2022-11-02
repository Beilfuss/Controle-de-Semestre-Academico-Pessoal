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

        colegas = self.obter_colegas_por_disc(disciplina_id)
        colegas_dados = [(colega.nome, colega.matricula) for colega in colegas]

        grupo = self.__dao.obter_por_id(atividade_id)
        if (grupo is None):
            grupo = self.__dao.criar_grupo(atividade_id)

        # extrair parte de baixo em uma função
        opcoes = {0: "", 1: lambda dados: self.adicionar_colega(grupo, colegas, dados),
                  2: lambda dados: self.excluir_colega(grupo, colegas, dados), 3: lambda dados: self.alterar_numero_colegas(grupo, dados)}

        while (True):

            membros_grupo = self.obter_colegas_do_grupo(colegas, grupo.colegas)
            opcao_escolhida, dados = self.__tela.abrir(
                disciplina_nome, grupo.numAlunos, colegas_dados, membros_grupo)

            if (opcao_escolhida != 0):
                opcao_escolhida, opcoes[opcao_escolhida](dados)
            else:
                return (opcao_escolhida, None)

    def obter_colegas_por_disc(self, disciplina_id):
        # obter colegas - id - atividade
        return self.__controlador_sistema.obter_colegas_por_disc(disciplina_id)

    def obter_colegas_do_grupo(self, colegas, colegas_grupo):

        colegas_grupo_obj = list(
            filter(lambda colega: colega.id in colegas_grupo, colegas))

        return [(colega.nome, colega.matricula) for colega in colegas_grupo_obj]

    def adicionar_colega(self, grupo, colegas, dados):
        index = dados["novo_colega_index"][0]
        colega = colegas[index]

        # Verifica se o colega já está no grupo
        if (grupo.is_membro(colega.id)):
            print("Colega já está no grupo")
        else:
            # Inclui o colega no grupo
            self.__dao.adiciona_membro(grupo, colega.id)

    def excluir_colega(self, grupo, colegas, dados):

        index = dados["row_index"][0]
        colega = colegas[index]

        self.__dao.remover_membro(grupo, colega.id)

    def alterar_numero_colegas(self, grupo, dados):

        numColegas = int(dados["numColegas"])

        if (numColegas < 2):
            return print("Número inválido")

        self.__dao.alterar_numero_colegas(grupo, numColegas)

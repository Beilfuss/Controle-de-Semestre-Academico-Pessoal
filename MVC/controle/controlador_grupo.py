from limite.tela_grupo import TelaGrupo
from dao.grupo_dao import GrupoDAO
from excecoes.membroRepetidoException import MembroRepetidoException
from excecoes.grupoCheioException import GrupoCheioException


'''
    Falta:
        Excluir colega da disciplina implica na exclusão de colega do grupo - Não dá para fazer
'''


class ControladorGrupo:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaGrupo(self)
        self.__dao = GrupoDAO()

    def cadastrar_grupo(self, disciplina_id, disciplina_nome, atividade_id):

        colegas = self.obter_colegas_por_disc(disciplina_id)
        grupo = self.__dao.obter_por_id(atividade_id)
        if (grupo is None):
            grupo = self.__dao.criar_grupo(atividade_id)

        colegas_recomendados = self.obter_colegas_recomendados(
            colegas, grupo.id)
        colegas_dados = self.destacar_colegas_recomendados(
            colegas, colegas_recomendados)

        self.exibir_tela_cadastro(
            disciplina_nome, grupo, colegas, colegas_dados)

    def obter_grupo_por_atividade(self, atividade_id):
        return self.__dao.obter_por_id(atividade_id)

    def obter_colegas_por_disc(self, disciplina_id):
        # obter colegas - id - atividade
        return self.__controlador_sistema.obter_colegas_por_disc(disciplina_id)

    def obter_colegas_recomendados(self, colegas, grupo_id):

        colegas_recomendados = []

        for colega in colegas:
            recomendado = self.__dao.exists_grupo_anterior(colega.id, grupo_id)
            if (recomendado):
                colegas_recomendados.append(colega)

        return colegas_recomendados

    def destacar_colegas_recomendados(self, colegas, colegas_recomendados):
        colegas_dados = []
        for colega in colegas:
            if colega in colegas_recomendados:
                colegas_dados.append(("{} (Recomendado)".format(
                    colega.nome), colega.matricula))
            else:
                colegas_dados.append((colega.nome, colega.matricula))

        return colegas_dados

    def obter_colegas_do_grupo(self, colegas, colegas_grupo):

        colegas_grupo_obj = list(
            filter(lambda colega: colega.id in colegas_grupo, colegas))

        return colegas_grupo_obj

    def exibir_tela_cadastro(self, disciplina_nome, grupo, colegas, colegas_dados):
        opcoes = {0: "", 1: lambda dados: self.adicionar_colega(grupo, colegas, dados),
                  2: lambda dados: self.excluir_colega(grupo, colegas, dados), 3: lambda dados: self.alterar_numero_alunos(grupo, dados)}

        while (True):

            membros_grupo = self.obter_colegas_do_grupo(colegas, grupo.colegas)
            membros_grupo_dados = [(colega.nome, colega.matricula)
                                   for colega in membros_grupo]

            opcao_escolhida, dados = self.__tela.abrir(
                disciplina_nome, grupo.numAlunos, colegas_dados, membros_grupo_dados)

            if (opcao_escolhida != 0):
                opcao_escolhida, opcoes[opcao_escolhida](dados)
            else:
                return (opcao_escolhida, None)

    def adicionar_colega(self, grupo, colegas, dados):
        index = dados["novo_colega_index"][0]
        colega = colegas[index]

        try:
            # Valida adição de colega
            self.validar_adicao(grupo, colega.id)
            # Inclui o colega no grupo
            self.__dao.adiciona_membro(grupo, colega.id)
        except Exception as err:
            self.__tela.mostrar_mensagem(err)

    def excluir_colega(self, grupo, colegas, dados):

        index = dados["row_index"][0]
        membros = self.obter_colegas_do_grupo(colegas, grupo.colegas)

        colega = membros[index]

        self.__dao.remover_membro(grupo, colega.id)

    def alterar_numero_alunos(self, grupo, dados):

        numAlunos = int(dados["numAlunos"])

        if (not grupo.is_num_valido(numAlunos)):
            return print("Número inválido")

        self.__dao.alterar_numero_colegas(grupo, numAlunos)

    def validar_adicao(self, grupo, colega_id):
        if (grupo.is_membro(colega_id)):
            raise MembroRepetidoException
        if grupo.is_cheio():
            raise GrupoCheioException

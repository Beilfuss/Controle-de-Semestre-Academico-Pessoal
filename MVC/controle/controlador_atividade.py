from limite.tela_atividade import TelaAtividade
from dao.atividade_dao import AtividadeDAO
from excecoes.validationException import ValidationException


class ControladorAtividade:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaAtividade(self)
        self.__dao = AtividadeDAO()

    def exibir_atividade(self, disciplina, atividade):

        atividade_display = atividade.desempacotar()

        opcoes = {1: lambda: self.cadastrar_grupo(
            disciplina.id, disciplina.nome, atividade.id)}

        while (True):

            colegas = self.obter_colegas_do_grupo(atividade.id)
            colegas_dados = [(colega.nome, colega.matricula)
                             for colega in colegas]

            botao, valores = self.__tela.abrir(
                disciplina.nome, colegas_dados, atividade_display)

            if (botao == 0):
                return (botao, None)
            else:
                opcoes[botao](self.atividade)

    def cadastrar_atividade(self, disciplina):
        while True:

            opcao_escolhida, dados = self.__tela.abrir_cadastro(
                disciplina.nome)

            if opcao_escolhida == 0:
                break

            return self.incluir_atividade(disciplina.id, dados)

    def incluir_atividade(self, disciplina_id, dados):

        try:
            nome = dados["nome"]
            peso = int(dados["peso"])

            # aprimorar validação
            if (not nome.isalpha() or peso < 0 or peso > 100):
                raise ValidationException

            atividade = self.__dao.persist_atividade(disciplina_id, dados)

            return atividade

        except ValidationException as err:
            self.__tela.mostrar_mensagem(err)

    def obter_por_disciplina(self, disciplina_id):
        return self.__dao.obter_por_disciplina(disciplina_id)

    def cadastrar_grupo(self, disciplina_id, disciplina_nome, atividade_id):
        self.__controlador_sistema.cadastrar_grupo(
            disciplina_id, disciplina_nome, atividade_id)

    def obter_colegas_do_grupo(self, atividade_id):
        return self.__controlador_sistema.obter_colegas_do_grupo(atividade_id)

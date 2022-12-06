from limite.tela_atividade import TelaAtividade
from dao.atividade_dao import AtividadeDAO
from excecoes.validationException import ValidationException


class ControladorAtividade:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaAtividade(self)
        self.__dao = AtividadeDAO()

    def exibir_atividade(self, disciplina, atividade):

        opcoes = {1: lambda: self.cadastrar_grupo(
            disciplina, atividade),
            2: lambda: self.priorizar(atividade),
            3: lambda: self.excluir_atividade(atividade),
            4: lambda: self.alterar_atividade(disciplina.nome, atividade),
            5: lambda: print("TODO")}

        while (True):

            atividade_display = atividade.desempacotar()
            colegas = self.obter_colegas_do_grupo(atividade.id)
            colegas_dados = [(colega.nome, colega.matricula)
                             for colega in colegas]

            botao, valores = self.__tela.abrir(
                disciplina.nome, colegas_dados, atividade_display)

            if (botao == "cancelar" or botao == 0):
                return (botao, None)
            else:
                opcoes[botao]()
                if (botao == 3):
                    return (0, None)

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

            if (not nome.replace(" ", "").isalpha() or peso < 0 or peso > 100):
                raise ValidationException

            atividade = self.__dao.persist_atividade(disciplina_id, dados)

            return atividade

        except ValidationException as err:
            self.__tela.mostrar_mensagem(err)

    def alterar_atividade(self, disciplina_nome, atividade):
        try:

            botao, dados = self.__tela.abrir_cadastro(
                disciplina_nome, atividade.desempacotar(), alterar=True)

            if (botao == 2):
                nome = dados["nome"]
                peso = dados["peso"]

                if (not nome.replace(" ", "").isalpha() or int(peso) < 0 or int(peso) > 100):
                    raise ValidationException

                self.__dao.alterar(atividade, dados)

        except ValidationException as err:
            self.__tela.mostrar_mensagem(err)

    def excluir_atividade(self, atividade):
        self.__dao.delete(atividade)

    def priorizar(self, atividade):
        try:
            self.__dao.priorizar(atividade)
        except Exception as err:
            self.__tela.mostrar_mensagem(err)

    def obter_por_disciplina(self, disciplina_id):
        return self.__dao.obter_por_disciplina(disciplina_id)

    def cadastrar_grupo(self, disciplina, atividade):

        if (atividade.grupo):
            self.__controlador_sistema.cadastrar_grupo(
                disciplina.id, disciplina.nome, atividade.id)
        else:
            self.__tela.mostrar_mensagem(
                "Não é possível cadastrar grupo porque o trabalho é individual.")

    def obter_colegas_do_grupo(self, atividade_id):
        return self.__controlador_sistema.obter_colegas_do_grupo(atividade_id)

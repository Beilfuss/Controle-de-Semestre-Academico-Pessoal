from limite.tela_atividade import TelaAtividade
from dao.atividade_dao import AtividadeDAO
from excecoes.validationException import ValidationException


class ControladorAtividade:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaAtividade(self)
        self.__dao = AtividadeDAO()

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

from limite.tela_atividade import TelaAtividade
from dao.atividade_dao import AtividadeDAO


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

            #validacao = self.verificar_validade(dados_disciplina)

            # if validacao == True:
            #    self.__dao.persist_disciplina(dados_disciplina)
            #    break

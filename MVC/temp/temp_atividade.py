from entidade.disciplina import Disciplina
from entidade.atividade import Atividade
from entidade.nota import Nota

from limite.tela_disciplina import TelaDisciplina
from temp.tela_atividade import TelaAtividade


class ControladorAtividadeTemp:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema

        self.atividade = Atividade(
            9999, "Ph", "Trabalho", "13/05/1992", Nota(0, 1), True, True)

        self.__tela_atividade = TelaAtividade(self)
        self.__tela_disciplina = TelaDisciplina(self)

    def ver_atividade(self, disciplina_id, disciplina_nome):

        colegas = self.obter_colegas_do_grupo(self.atividade.id)
        colegas_dados = [(colega.nome, colega.matricula)
                         for colega in colegas]

        
        opcoes = {1: lambda atividade: self.cadastrar_grupo(
            disciplina_id, disciplina_nome, atividade.id)}

        while (True):
            botao, valores = self.__tela_atividade.abrir(
                disciplina_nome, colegas_dados)
            self.__tela_disciplina.fechar()

            if botao != 0 and botao is not None:
                opcoes[botao](self.atividade)
                break

            break

    def cadastrar_grupo(self, disciplina_id, disciplina_nome, atividade_id):
        self.__controlador_sistema.cadastrar_grupo(
            disciplina_id, disciplina_nome, atividade_id)

    def obter_colegas_do_grupo(self, atividade_id):
        return self.__controlador_sistema.obter_colegas_do_grupo(atividade_id)

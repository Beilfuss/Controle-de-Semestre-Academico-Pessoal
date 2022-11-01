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

        self.disciplina = Disciplina(9999, "Placeholder", "INE9999", "Fausto", 5, "Sim", [
        ], [], [self.atividade], [], "Sim")

        self.__tela_atividade = TelaAtividade(self)
        self.__tela_disciplina = TelaDisciplina(self)
        # self.__dao = AtividadeDAO()

    def inicializar(self):

        opcoes = {
            "Alterar Disciplina": lambda disciplina: print("placeholder"),
            "Excluir Disciplina": lambda disciplina: print("placeholder"),
            "Colegas": lambda disciplina: print("placeholder"),
            "Encerrar Disciplina": lambda disciplina: print("placeholder"),
            "Ver Atividade": lambda disciplina: self.ver_atividade(disciplina)
        }
        dados_disciplina = self.disciplina.desempacotar()

        while (True):
            botao, valores = self.__tela_disciplina.abrir(dados_disciplina)
            self.__tela_disciplina.fechar()

            if botao != "Voltar" and botao is not None:
                opcoes[botao](self.disciplina)
                break

            break

    def ver_atividade(self, disciplina):

        opcoes = {1: lambda atividade: self.cadastrar_grupo(
            disciplina, atividade.id)}

        while (True):
            botao, valores = self.__tela_atividade.abrir(disciplina.nome)
            self.__tela_disciplina.fechar()

            if botao != "0" and botao is not None:
                print(botao)
                opcoes[botao](self.atividade)
                break

            break

    def cadastrar_grupo(self, disciplina, atividade_id):
        self.__controlador_sistema.cadastrar_grupo(disciplina, atividade_id)

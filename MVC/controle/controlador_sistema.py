from limite.tela_inicial import TelaInicial
from controle.controlador_disciplina import ControladorDisciplina
from controle.controlador_colega import ControladorColega


class ControladorSistema:

    def __init__(self):
        self.__tela_inicial = TelaInicial(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_colega = ControladorColega(self)

    def inicializar_sistema(self):
        self.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def inicializar_colegas(self, nome_disciplina, colegas):
        return self.__controlador_colega.inicializar(nome_disciplina, colegas)

    def cadastrar_disciplina(self):
        self.__controlador_disciplina.incluir_disciplina()

    def associar_colega_disciplina(self, disciplina_id, colega_id):
        self.__controlador_disciplina.incluir_colega(disciplina_id, colega_id)

    def cadastrar_grupo(self, atividade_id=1):
        self.__controlador_grupo.cadastrar_grupo(atividade_id)

    def abrir_tela(self):

        dict_opcoes = {'Cadastrar Disciplina': self.cadastrar_disciplina,
                       'Finalizar Sistema': self.encerrar_sistema}

        while True:
            disciplinas = self.__controlador_disciplina.listar_disciplinas()

            opcao_escolhida = self.__tela_inicial.abrir(disciplinas)

            if (opcao_escolhida is None):
                exit(0)

            if (isinstance(opcao_escolhida, int)):
                self.__controlador_disciplina.abrir_tela_disciplina(
                    disciplinas[opcao_escolhida])

            else:
                funcao_escolhida = dict_opcoes[opcao_escolhida]
                funcao_escolhida()

            self.__tela_inicial.close()

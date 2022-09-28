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

    def cadastrar_disciplina(self):
        self.__controlador_disciplina.incluir_disciplina()
        self.__tela_inicial.close()

    def abrir_tela(self):
        dict_opcoes = {'Cadastrar Disciplina': self.cadastrar_disciplina,
                       'Colegas': self.__controlador_colega.inicializar,
                       'Finalizar Sistema': self.encerrar_sistema}

        while True:
            opcao_escolhida = self.__tela_inicial.abrir()
            funcao_escolhida = dict_opcoes[opcao_escolhida]
            funcao_escolhida()

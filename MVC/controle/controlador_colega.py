from limite.tela_colega import TelaColega
from entidade.colega import Colega

# Cadastrar Colegas
#   Associar Colega a disciplina
# Excluir Colega
#
#


class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaColega(self)
        self.__colegas = []

    def inicializar(self):

        opcoes = {0: "", 1: self.excluir_colega, 2: self.cadastrar_colega}

        opcao_escolhida, dados = self.listar_colegas()

        if(opcao_escolhida != 0):
            opcoes[opcao_escolhida](dados)

    def listar_colegas(self):
        botao, dados = self.__tela.abrir(self.unpack_todos())

        return botao, dados

    def cadastrar_colega(self, dados):

        nome = dados["nome"]
        if(not self.colega_cadastrado(nome)):
            colega = Colega(nome)
            self.__colegas.append(colega)
        else:
            self.__tela.mostrar_mensagem("Colega já cadastrado!")
        
        self.inicializar()

    def excluir_colega(self, nome):
        return

    def colega_cadastrado(self, nome):

        colegas_filtrado = list(
            filter(lambda colega: colega.nome == nome, self.__colegas))
        return len(colegas_filtrado) != 0

    def unpack(self, colega):
        return colega.nome

    def unpack_todos(self):
        return list(map(self.unpack, self.__colegas))

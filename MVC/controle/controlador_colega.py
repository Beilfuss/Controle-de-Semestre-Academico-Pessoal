from limite.tela_colega import TelaColega
from entidade.colega import Colega
from dao.colega_dao import ColegaDAO

#
# Associar Colega a disciplina
#


class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaColega(self)
        self.__dao = ColegaDAO()
        self.__colegas = []

    def inicializar(self):

        self.__dao.create_table()

        opcoes = {0: "", 1: self.excluir_colega, 2: self.cadastrar_colega}

        opcao_escolhida, dados = self.listar_colegas()

        if(opcao_escolhida != 0):
            opcoes[opcao_escolhida](dados)

    def listar_colegas(self):
        botao, dados = self.__tela.abrir(self.unpack_todos())

        return botao, dados

    def cadastrar_colega(self, dados):

        nome = dados["nome"]
        sucesso = self.__dao.persist_colega(nome)

        if(not sucesso):
            self.__tela.mostrar_mensagem("Colega já cadastrado!")

        self.inicializar()

    def excluir_colega(self, dados):

        try:
            index = dados["row_index"][0]
            self.__dao.delete_colega(index)
        except Exception as err:
            print(err)
            self.__tela.mostrar_mensagem(
                "É necessário selecionar um colega para exclusão")
        finally:
            self.inicializar()

    def unpack(self, colega):
        return colega.nome

    def unpack_todos(self):
        return list(map(self.unpack, self.__dao.buscar_todos()))

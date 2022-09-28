from limite.tela_colega import TelaColega

# Listar Colegas
# Cadastrar Colegas
#   Associar Colega a disciplina
# Excluir Colega
#
#


class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaColega(self)
        self.__colegas = [{"nome": "teste1"}, {"nome": "teste4"}]

    def cadastrar_colega(self):
        return

    def listar_colegas(self):
        self.__tela.abrir(self.unpack_todos())

    def unpack(self, colega):
        return colega["nome"]

    def unpack_todos(self):
        return list(map(self.unpack, self.__colegas))

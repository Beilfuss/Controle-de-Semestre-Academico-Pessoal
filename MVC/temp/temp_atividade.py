from entidade.atividade import Atividade
from entidade.nota import Nota


class ControladorAtividade:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        #self.__tela = TelaAtividade(self)
        #self.__dao = AtividadeDAO()

    def inicializar(self):

        atividade = Atividade(
            "Ph", "Trabalho", "13/05/1992", Nota(0, 1), True, False)
        

        opcoes = {0: "", 1: lambda : self.cadastrar_grupo()}
    

    def cadastrar_grupo(self):
        self.__controlador_sistema.cadastrar_grupo()

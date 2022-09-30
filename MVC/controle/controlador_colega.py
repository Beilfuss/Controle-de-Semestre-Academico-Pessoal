from limite.tela_colega import TelaColega
from dao.colega_dao import ColegaDAO

#
# Associar Colega a disciplina
#


class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaColega(self)
        self.__dao = ColegaDAO()

    def inicializar(self):

        opcoes = {0: "", 1: self.excluir_colega, 2: self.cadastrar_colega}

        opcao_escolhida, dados = self.listar_colegas()

        if(opcao_escolhida != 0):
            opcoes[opcao_escolhida](dados)

    def listar_colegas(self):
        botao, dados = self.__tela.abrir(self.desempacotar_todos())

        return botao, dados

    def cadastrar_colega(self, dados):

        try:
            nome = dados["nome"]
            matricula = dados["matricula"]
            if(not nome.isalpha() or len(matricula) != 8 or not matricula.isdecimal()):
                raise ValueError

            sucesso = self.__dao.persist_colega(nome, matricula)

            if(not sucesso):
                self.__tela.mostrar_mensagem("Colega já cadastrado!")
        except ValueError:
            self.__tela.mostrar_mensagem("Dados inválidos! Tente novamente.")
        finally:
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

    def desempacotar_todos(self):
        return list(map(lambda colega: colega.desempacotar(), self.__dao.buscar_todos()))

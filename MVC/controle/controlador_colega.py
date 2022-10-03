from limite.tela_colega import TelaColega
from dao.colega_dao import ColegaDAO

class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaColega(self)
        self.__dao = ColegaDAO()

    def inicializar(self, nome_disciplina, colegas):

        colegas_obj = [self.__dao.obter_por_id(id) for id in colegas]
        
        opcoes = {0: "", 1: lambda dados: self.excluir_colega(colegas_obj, dados), 2:self.cadastrar_colega}

        opcao_escolhida, dados = self.listar_colegas(nome_disciplina, colegas_obj)

        if(opcao_escolhida != 0):
            return (opcao_escolhida, opcoes[opcao_escolhida](dados))
        else:
            return (opcao_escolhida, None)

    def listar_colegas(self, nome_disciplina, colegas):
        botao, dados = self.__tela.abrir(nome_disciplina, self.desempacotar_todos(colegas))

        return botao, dados

    def cadastrar_colega(self, dados):

        try:
            nome = dados["nome"]
            matricula = dados["matricula"]
            if(not nome.isalpha() or len(matricula) != 8 or not matricula.isdecimal()):
                raise ValueError

            colega = self.__dao.obter_por_matricula(matricula)

            if(colega is None):
                colega = self.__dao.persist_colega(nome, matricula)

            return colega

        except ValueError:
            self.__tela.mostrar_mensagem("Dados inválidos! Tente novamente.")
            

    def excluir_colega(self, colegas, dados):

        index = dados["row_index"][0]
        colega = colegas[index]
        return colega

    def desempacotar_todos(self, colegas):
        return list(map(lambda colega: colega.desempacotar(), colegas))

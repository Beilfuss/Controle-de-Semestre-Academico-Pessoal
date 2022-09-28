from limite.tela_dados_disciplina import TelaDadosDisciplina
# from MVC.limite.tela_disciplina import TelaDisciplina
# from MVC.entidade.disciplina import Disciplina


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        # self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)

    def incluir_disciplina(self, values=None):
        while True:
            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(
                dados_disciplina={"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "recuperacao": ""}
            )

            self.__tela_dados_disciplina.fechar()


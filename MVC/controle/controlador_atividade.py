from limite.tela_atividade import TelaAtividade
from limite.tela_dados_atividade import TelaDadosAtividade

class ControladorAtividade():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_dados_atividade = TelaDadosAtividade()
        self.__tela_atividade = TelaAtividade()

    def incluir_atividade(self):
        while True:
            botao, dados_atividade = self.__tela_dados_atividade.abrir(
                dados_disciplina={"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "recuperacao": ""}
            )

            self.__tela_dados_disciplina.fechar()

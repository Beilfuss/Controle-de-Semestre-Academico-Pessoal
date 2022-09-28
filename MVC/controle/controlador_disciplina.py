from MVC.limite.tela_dados_disciplina import TelaDadosDisciplina
from MVC.limite.tela_disciplina import TelaDisciplina
from MVC.entidade.disciplina import Disciplina
from MVC.entidade.professor import Professor


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)

    def incluir_disciplina(self, values=None):
        while True:
            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(
                dados_disciplina={"nome": "", "codigo": "", "professor": "",
                               "numAulas": "", "rec": ""})

            self.__tela_dados_disciplina.fechar()

            try:
                int(dados_disciplina["numAulas"])
                if dados_disciplina == {"nome": "", "codigo": "", "professor": "", "numero_aulas": ""
                                        #"rec": ???
                } or (dados_disciplina["nome"]).isdigit() or (dados_disciplina["professor"]).isdigit() or \
                (dados_disciplina["numAulas"]).isalpha():
                    raise ValueError
                    # VERIFICAR SE A DISCIPLINA JÁ EXISTE

                professor = Professor(dados_disciplina["nome"])

                if dados_disciplina[0]:
                    dados_disciplina["rec"] = True
                else:
                    dados_disciplina["rec"] = False

                disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["codigo"], professor,
                                        dados_disciplina["numAulas"], dados_disciplina["rec"], None, None, None, None)

                print("Disciplina: ", disciplina)
                # PERSISTÊNCIA

                break

            except ValueError:
                self.__tela_disciplina.mostrar_mensagem("Atenção","Dados inválidos. Tente novamente!")
                continue



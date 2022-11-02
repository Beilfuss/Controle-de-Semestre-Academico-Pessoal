from limite.tela_colega import TelaColega
from dao.colega_dao import ColegaDAO
from excecoes.validationException import ValidationException
from excecoes.matriculaRepetidaException import MatriculaRepetidaException


class ControladorColega:

    def __init__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaColega(self)
        self.__dao = ColegaDAO()

    def inicializar(self, nome_disciplina, colegas):

        colegas_obj = [self.__dao.obter_por_id(id) for id in colegas]

        opcoes = {0: "", 1: lambda dados: self.excluir_colega(
            colegas_obj, dados), 2: self.cadastrar_colega, 3: lambda dados: self.alterar_colega(colegas_obj, dados)}

        opcao_escolhida, dados = self.listar_colegas(
            nome_disciplina, colegas_obj)

        if (opcao_escolhida != 0):
            return (opcao_escolhida, opcoes[opcao_escolhida](dados))
        else:
            return (opcao_escolhida, None)

    def obter_colega_por_disc(self, disciplina_id):
        return self.__dao.obter_por_disc(disciplina_id)

    def listar_colegas(self, nome_disciplina, colegas):
        botao, dados = self.__tela.abrir(
            nome_disciplina, self.desempacotar_todos(colegas))

        return botao, dados

    def cadastrar_colega(self, dados):

        try:
            nome = dados["nome"]
            matricula = dados["matricula"]
            if (not nome.isalpha() or len(matricula) != 8 or not matricula.isdecimal()):
                raise ValidationException

            colega = self.__dao.obter_por_matricula(matricula)

            if (colega is not None and colega.nome != nome):
                raise MatriculaRepetidaException(
                    "Já há aluno cadastrado com a matrícula informada, mas outro nome. Nome: {}".format(colega.nome))

            if (colega is None):
                colega = self.__dao.persist_colega(nome, matricula)

            return colega

        except ValidationException as err:
            self.__tela.mostrar_mensagem(err)
        except MatriculaRepetidaException as err:
            self.__tela.mostrar_mensagem(err)

    def alterar_colega(self, colegas, dados):
        try:
            index = dados["row_index"][0]
            colega = colegas[index]

            botao, dados = self.__tela.abrir_alteracao(
                colega.matricula, colega.nome)

            if (botao == 1):
                nome = dados["nome"]

                if (not nome.isalpha()):
                    raise ValidationException

                self.__dao.alterar_colega(colega, nome)

        except ValidationException as err:
            self.__tela.mostrar_mensagem(err)
        except IndexError:
            self.__tela.mostrar_mensagem("É necessário selecionar um colega!")

    def excluir_colega(self, colegas, dados):

        try:
            index = dados["row_index"][0]
            colega = colegas[index]
            return colega
        except IndexError:
            self.__tela.mostrar_mensagem("É necessário selecionar um colega!")

    def desempacotar_todos(self, colegas):
        return list(map(lambda colega: colega.desempacotar(), colegas))

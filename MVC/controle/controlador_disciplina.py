from limite.tela_dados_disciplina import TelaDadosDisciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina
from dao.disciplina_dao import DisciplinaDAO
from excecoes.jaExistenteException import JaExistenteException


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)
        self.__dao = DisciplinaDAO()

    def listar_disciplinas(self):
        return [disciplina.desempacotar() for disciplina in self.__dao.buscar_todos()]

    def abrir_tela_disciplina(self, dados_disciplina):

        while (True):
            disciplina = self.__dao.obter_por_id(dados_disciplina["id"])

            botao, valores = self.__tela_disciplina.abrir(dados_disciplina)

            self.__tela_disciplina.fechar()

            opcoes = {
                "Alterar Disciplina": lambda disciplina: self.alterar_disciplina(disciplina, dados_disciplina),
                "Excluir Disciplina": lambda disciplina: self.excluir_disciplina(disciplina.id),
                "Colegas": lambda disciplina: self.abrir_tela_colegas(disciplina),
                'UseCase Grupo': lambda disciplina: self.__controlador_sistema.abrir_tela_temp(disciplina.id, disciplina.nome),
                "Encerrar Disciplina": lambda disciplina: self.encerrar_disciplina(disciplina.id)
            }

            if botao != "Voltar" and botao is not None:
                opcoes[botao](disciplina)
                break

            break

    def abrir_tela_colegas(self, disciplina):

        opcoes = {0: "", 1: lambda colega: self.remover_colega(
            disciplina, colega), 2: lambda colega: self.incluir_colega(disciplina, colega)}

        (operacao, colega) = self.__controlador_sistema.inicializar_colegas(
            disciplina.nome, disciplina.colegas)

        if (operacao != 0):

            if (colega is not None):
                opcoes[operacao](colega)
            self.abrir_tela_colegas(disciplina)

    def incluir_disciplina(self):

        while True:

            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(dados_disciplina={"nome": "", "codigo": "", "professor": "",
                                                                                           "numAulas": "", "rec": ""})

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break

            validacao = self.verificar_validade(dados_disciplina)

            if validacao == True:
                self.__dao.persist_disciplina(dados_disciplina)
                break

    def alterar_disciplina(self, disciplina, dados_disciplina):

        while True:

            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(
                dados_disciplina)

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break

            validacao = self.verificar_validade(dados_disciplina)

            if validacao == True:
                dados_disciplina['id'] = disciplina.id
                self.__dao.alterar_disciplina(dados_disciplina)
                break

    def excluir_disciplina(self, id):
        self.__dao.delete_disciplina(id)

    def encerrar_disciplina(self, id):
        self.__dao.encerrar_disciplina(id)

    def verificar_validade(self, dados_disciplina):
        try:
            dados_disciplina['numAulas'] = int(dados_disciplina["numAulas"])

            if dados_disciplina[0]:
                dados_disciplina["rec"] = "Sim"  # Tem REC
            else:
                dados_disciplina["rec"] = "Não"  # Não tem REC

            if dados_disciplina == {"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "rec": ""} \
                    or (not (all(char.isalpha() or char.isspace() for char in dados_disciplina['nome']))) \
                    or (not (all(char.isalpha() or char.isspace() for char in dados_disciplina['professor']))) \
                    or (dados_disciplina['codigo'].isalpha()) or (dados_disciplina['codigo'].isdigit()):
                raise ValueError

            disciplinas = self.__dao.buscar_todos()
            for disciplina in disciplinas:
                if disciplina.codigo == dados_disciplina['codigo'] and disciplina.ativo == "Sim":
                    raise JaExistenteException

            return True

        except ValueError:
            self.__tela_disciplina.mostrar_mensagem(
                "Atenção", "Dados inválidos. Tente novamente!")
            return False
        except JaExistenteException:
            self.__tela_disciplina.mostrar_mensagem(
                'Atenção', 'Disciplina já existente, tente novamente!')
            return False

    def incluir_colega(self, disciplina, colega):
        sucesso = self.__dao.incluir_colega(disciplina, colega)

        if (not sucesso):
            self.__tela_disciplina.mostrar_mensagem(
                "Atenção", "Colega já cadastrado!")

    def remover_colega(self, disciplina, colega):

        sucesso = self.__dao.remover_colega(disciplina, colega)
        return

import datetime
import functools
from limite.tela_dados_disciplina import TelaDadosDisciplina
from limite.tela_disciplina import TelaDisciplina
from limite.tela_faltas import TelaFaltas
from dao.disciplina_dao import DisciplinaDAO
from excecoes.jaExistenteException import JaExistenteException


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)
        self.__tela_faltas = TelaFaltas(self)
        self.__dao = DisciplinaDAO()

    def listar_disciplinas(self):
        return [disciplina.desempacotar() for disciplina in self.__dao.buscar_todos()]

    def abrir_tela_disciplina(self, dados_disciplina):

        while (True):
            try:

                disciplina = self.__dao.obter_por_id(dados_disciplina["id"])
                atividades = self.__controlador_sistema.obter_atividades_da_disciplina(
                    disciplina.id)
                atividades_dados = [atividade.desempacotar()
                                    for atividade in atividades]

                atividades_peso_total = functools.reduce(
                    lambda total, atividade: total+atividade.peso_nota, atividades, 0)

                dicts_aulas_de_disciplina = self.gerir_aulas(
                    disciplina, None, "Obter Aulas")
                dados_disciplina['aulas'] = dicts_aulas_de_disciplina

                aulas = dados_disciplina['aulas']
                dados_tabela = []
                for aula in aulas:
                    for horario in aula['horario']:
                        dados_tabela.append(
                            [aula['dia'], horario[0], aula['sala']])
                dados_disciplina['aulas'] = dados_tabela

                botao, valores = self.__tela_disciplina.abrir(
                    dados_disciplina, atividades_dados, atividades_peso_total != 100)

                if valores['row_aula_index'] != []:
                    aula_selecionada = dados_disciplina['aulas'][valores['row_aula_index'][0]]

                self.__tela_disciplina.fechar()

                if (botao == 'Alterar Aula' or botao == 'Excluir Aula') and valores['row_aula_index'] == []:
                    raise ValueError

                opcoes = {
                    "Alterar Disciplina": lambda disciplina: self.alterar_disciplina(disciplina, dados_disciplina),
                    "Excluir Disciplina": lambda disciplina: self.excluir_disciplina(disciplina.id),
                    "Cadastrar Aula": lambda disciplina: self.gerir_aulas(disciplina, None, "Cadastrar Aula"),
                    "Alterar Aula": lambda disciplina: self.gerir_aulas(disciplina, aula_selecionada, "Alterar Aula"),
                    "Excluir Aula": lambda disciplina: self.gerir_aulas(disciplina, aula_selecionada, "Excluir Aula"),
                    "Colegas": lambda disciplina: self.abrir_tela_colegas(disciplina),
                    "Cadastrar Atividade": lambda disciplina: self.__controlador_sistema.cadastrar_atividade(disciplina),
                    "Ver Atividade": lambda disciplina: self.ver_atividade(disciplina, atividades, valores["row_index"]),
                    "Encerrar Disciplina": lambda disciplina: self.encerrar_disciplina(disciplina.id),
                    "Registrar Faltas": lambda disciplina: self.registrar_faltas(disciplina)
                }

                if botao == "Voltar" or botao is None:
                    break

                opcoes[botao](disciplina)

            except ValueError:
                self.__tela_disciplina.mostrar_mensagem(
                    "Atenção", "Nenhuma aula selecionada!")

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

            validacao = self.verificar_validade_disciplina(dados_disciplina)

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

            validacao = self.verificar_validade_disciplina(dados_disciplina)

            if validacao == True:
                dados_disciplina['id'] = disciplina.id
                self.__dao.alterar_disciplina(dados_disciplina)
                break

    def excluir_disciplina(self, id):
        id_aulas_para_excluir = self.__dao.delete_disciplina(id)
        if id_aulas_para_excluir is not None:
            self.__controlador_sistema.remover_aulas_cache(
                id_aulas_para_excluir)

    def encerrar_disciplina(self, id):
        self.__dao.encerrar_disciplina(id)

    def verificar_validade_disciplina(self, dados_disciplina):
        try:

            if dados_disciplina[0]:
                dados_disciplina["rec"] = "Sim"  # Tem REC
            else:
                dados_disciplina["rec"] = "Não"  # Não tem REC
            dados_disciplina['numAulas'] = int(dados_disciplina["numAulas"])

            # REVISAR VERIFICAÇÕES
            if dados_disciplina["nome"] == "" or dados_disciplina["codigo"] == "" or dados_disciplina["professor"] == "" \
                    or dados_disciplina["numAulas"] == "" or dados_disciplina["rec"] == "" \
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

    def ver_atividade(self, disciplina, atividades, index):

        try:
            atividade = atividades[index[0]]
            self.__controlador_sistema.exibir_atividade(disciplina, atividade)
        except IndexError:
            self.__tela_disciplina.mostrar_mensagem("Atenção",
                                                    "É necessário selecionar uma atividade!")

    def incluir_colega(self, disciplina, colega):
        sucesso = self.__dao.incluir_colega(disciplina, colega)

        if (not sucesso):
            self.__tela_disciplina.mostrar_mensagem(
                "Atenção", "Colega já cadastrado!")

    def remover_colega(self, disciplina, colega):

        sucesso = self.__dao.remover_colega(disciplina, colega)
        return

    def gerir_aulas(self, disciplina, aula_selecionada, opcao):
        if opcao == "Obter Aulas":
            return self.__controlador_sistema.gerir_aulas(disciplina, aula_selecionada, opcao)
        else:
            self.__controlador_sistema.gerir_aulas(
                disciplina, aula_selecionada, opcao)

    def registrar_faltas(self, disciplina):

        while True:

            try:

                faltas = []
                for falta in disciplina.faltas:
                    faltas.append([falta.dia, falta.numFaltas])

                dados_faltas = {'nome': disciplina.nome, 'faltas': faltas}

                botao, valores = self.__tela_faltas.abrir(dados_faltas)

                self.__tela_faltas.fechar()

                if botao == "Voltar":
                    break

                elif botao == "Cadastrar Faltas":

                    if valores['dia'] == "" or valores['numFaltas'] == "":
                        raise ValueError

                    valores['numFaltas'] = int(valores['numFaltas'])

                    data = self.validar_data_falta(valores['dia'])
                    if valores['numFaltas'] > 10 or not data:
                        raise ValueError

                    dados_faltas = {"disciplina_id": disciplina.id, "dia": valores['dia'], "numFaltas": valores['numFaltas']}
                    self.__dao.persist_faltas(dados_faltas)

                    self.checar_risco_faltas(disciplina)

                elif botao == "Excluir Falta":
                    if valores['row_falta_index'] == []:
                        raise Exception
                    else:

                        for falta in disciplina.faltas:
                            if falta.dia == faltas[valores['row_falta_index'][0]][0] and falta.numFaltas == faltas[valores['row_falta_index'][0]][1]:
                                id = falta.id
                                disciplina_id = falta.disciplina_id

                        self.__dao.delete_falta(id, disciplina_id)
                
            except ValueError:
                self.__tela_disciplina.mostrar_mensagem("Atenção!", "Dados inválidos. Tente novamente!")
            except Exception:
                self.__tela_disciplina.mostrar_mensagem("Atenção!", "Nenhuma falta selecionada!")

    def validar_data_falta(self, data):
    
        try:
        
            if len(data) > 10:
                raise ValueError
            elif data[2:3] != "/" or data[5:6] != "/":
                raise ValueError
            
            dia = int(data[0:2])
            mes = int(data[3:5])
            ano = int(data[6:10])
            
            hoje = datetime.date.today()
            ano_atual = hoje.year
            
            if dia < 1 or dia > 31:
                raise ValueError
            elif mes < 1 or mes > 12:
                raise ValueError
            elif ano != ano_atual:
                raise ValueError
            else:
                return True
            
        except ValueError:
            self.__tela_disciplina.mostrar_mensagem("Atenção!", "Dados inválidos. Tente novamente!")
            return False

    def checar_risco_faltas(self, disciplina):
        
        total_faltas = 0
        for falta in disciplina.faltas:
            total_faltas += falta.numFaltas

        faltas_possiveis = int(disciplina.numAulas * 0.25)
        faltas_restantes = faltas_possiveis - total_faltas

        if total_faltas == faltas_possiveis or total_faltas < faltas_possiveis and faltas_restantes <= 3:
            self.__tela_disciplina.mostrar_mensagem("Atenção!", "Risco de reprovação por falta na disciplina {nome}! Você tem apenas {numero} falta(s) restante(s)!".format(nome=disciplina.nome, numero=faltas_restantes))
        elif total_faltas > faltas_possiveis:
            self.__tela_disciplina.mostrar_mensagem("Atenção!", "Você está reprovado por falta na disciplina {nome}.".format(nome=disciplina.nome))
    

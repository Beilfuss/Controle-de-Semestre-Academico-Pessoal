from limite.tela_inicial import TelaInicial
from controle.controlador_disciplina import ControladorDisciplina
from controle.controlador_colega import ControladorColega
from controle.controlador_aula import ControladorAula
from controle.controlador_grupo import ControladorGrupo
from controle.controlador_atividade import ControladorAtividade



class ControladorSistema:

    def __init__(self):
        self.__tela_inicial = TelaInicial(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_atividade = ControladorAtividade(self)
        self.__controlador_colega = ControladorColega(self)
        self.__controlador_grupo = ControladorGrupo(self)

        self.__controlador_aula = ControladorAula(self)

    def inicializar_sistema(self):
        self.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def inicializar_colegas(self, nome_disciplina, colegas):
        return self.__controlador_colega.inicializar(nome_disciplina, colegas)

    def cadastrar_disciplina(self):
        self.__controlador_disciplina.incluir_disciplina()

    def cadastrar_atividade(self, disciplina):
        self.__controlador_atividade.cadastrar_atividade(disciplina)

    def popular_colegas(self, colegas_ids):
        return self.__controlador_colega.obter_colegas(colegas_ids)

    def obter_colegas_por_disc(self, disciplina_id):
        return self.__controlador_colega.obter_colega_por_disc(disciplina_id)

    def associar_colega_disciplina(self, disciplina_id, colega_id):
        self.__controlador_disciplina.incluir_aula(disciplina_id, colega_id)
   
    def gerir_aulas(self, disciplina, aula_selecionada, opcao):
        if opcao == "Obter Aulas":
            return self.__controlador_aula.gerir_aulas(disciplina, aula_selecionada, opcao)
        else:
            self.__controlador_aula.gerir_aulas(disciplina, aula_selecionada, opcao)

    def remover_aulas_cache(self, id_aulas_para_excluir):
        self.__controlador_aula.remover_aulas_cache(id_aulas_para_excluir)   
    
    def exibir_atividade(self, disciplina, atividade):
        self.__controlador_atividade.exibir_atividade(disciplina, atividade)


    def cadastrar_grupo(self, disciplina_id, disciplina_nome, atividade_id):
        self.__controlador_grupo.cadastrar_grupo(
            disciplina_id, disciplina_nome, atividade_id)

    def obter_colegas_do_grupo(self, atividade_id):
        grupo = self.__controlador_grupo.obter_grupo_por_atividade(
            atividade_id)

        if (grupo):
            return self.popular_colegas(grupo.colegas)
        else:
            return []

    def obter_atividades_da_disciplina(self, disciplina_id):
        return self.__controlador_atividade.obter_por_disciplina(disciplina_id)

    def abrir_tela(self):

        dict_opcoes = {'Cadastrar Disciplina': self.cadastrar_disciplina,
                       'Finalizar Sistema': self.encerrar_sistema}

        while True:
            disciplinas = self.__controlador_disciplina.listar_disciplinas()

            opcao_escolhida = self.__tela_inicial.abrir(disciplinas)

            if (opcao_escolhida is None):
                exit(0)

            if (isinstance(opcao_escolhida, int)):
                self.__controlador_disciplina.abrir_tela_disciplina(
                    disciplinas[opcao_escolhida])

            else:
                funcao_escolhida = dict_opcoes[opcao_escolhida]
                funcao_escolhida()

            self.__tela_inicial.close()

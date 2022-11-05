from limite.tela_inicial import TelaInicial
from controle.controlador_disciplina import ControladorDisciplina
from controle.controlador_colega import ControladorColega
from controle.controlador_aula import ControladorAula


class ControladorSistema:

    def __init__(self):
        self.__tela_inicial = TelaInicial(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_colega = ControladorColega(self)
        self.__controlador_aula = ControladorAula(self)

    def inicializar_sistema(self):
        self.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def inicializar_colegas(self, nome_disciplina, colegas):
        return self.__controlador_colega.inicializar(nome_disciplina, colegas)

    def cadastrar_disciplina(self):
        self.__controlador_disciplina.incluir_disciplina()

    def associar_colega_disciplina(self, disciplina_id, colega_id):
        self.__controlador_disciplina.incluir_aula(disciplina_id, colega_id)
   
    def gerir_aulas(self, disciplina, opcao):
        opcoes = {'Cadastrar Aula': self.__controlador_aula.cadastrar_aula,
                  #'Alterar Aula': self.__controlador_aula.alterar_aula,
                  #'Excluir Aula': lambda disciplina: self.__controlador_aula.excluir_aula,
                  'Obter Aulas': self.__controlador_aula.obter_aulas_de_disciplina
                  }
        
        if opcao == 'Obter Aulas':
            return opcoes[opcao](disciplina)
        else:
            opcoes[opcao](disciplina)

    def abrir_tela(self):

        dict_opcoes = {'Cadastrar Disciplina': self.cadastrar_disciplina,
                       'Finalizar Sistema': self.encerrar_sistema}

        while True:
            disciplinas = self.__controlador_disciplina.listar_disciplinas()

            print('disciplinas: ', disciplinas)

            opcao_escolhida = self.__tela_inicial.abrir(disciplinas)

            if(opcao_escolhida is None):
                exit(0)

            if (isinstance(opcao_escolhida, int)):
                self.__controlador_disciplina.abrir_tela_disciplina(disciplinas[opcao_escolhida])
                
            else:
                funcao_escolhida = dict_opcoes[opcao_escolhida]
                funcao_escolhida()
            
            self.__tela_inicial.close()

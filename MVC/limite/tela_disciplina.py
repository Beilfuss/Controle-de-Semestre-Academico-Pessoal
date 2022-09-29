import PySimpleGUI as sg

class TelaDisciplina():

    def __init__(self, controlador_disciplina):
        self.__controlador_disciplina = controlador_disciplina
        self.__janela = None
        self.inicializar_componentes()

    def inicializar_componentes(self, dados_disciplinas=None):
        if dados_disciplinas is None:
            dados_disciplinas = {'nome': '', 'codigo': '', 'professor': '', 'numAulas': '',
                                 0: '', 1: '', 'rec': ''}

        layout = [
            [sg.Text("{codigo} - {nome}".format(codigo=dados_disciplinas['codigo'],nome=dados_disciplinas['nome']))],
            [sg.Text("Professor: {professor}".format(professor=dados_disciplinas['professor']))],
            [sg.Text("Recuperação: {professor}".format(professor=dados_disciplinas['professor']))],
            [sg.Text("Média Parcial: ")],
            [sg.Text("Faltas Remanescentes: ")],
            [sg.Submit(button_text="Colegas"), sg.Submit(button_text="Registrar Falta")],
            [sg.Text("")],
            [sg.Text("Lista de Atividades")],
            [sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
            [sg.Submit(button_text="Ver Atividade"), sg.Submit(button_text="Cadastrar Atividade")],
            [sg.Text("")],
            [sg.Text("Aulas")],
            [sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
            [sg.Submit(button_text="Cadastrar Aula")],
            [sg.Submit(button_text="Excluir Disciplina"), sg.Submit(button_text="Alterar Disciplina"),
             sg.Submit(button_text="Voltar")]
        ]

        self.__janela = sg.Window("TelaDisciplina", default_element_size=(40, 1)).Layout(layout)

    def abrir(self, dados_disciplina=[]):
        self.inicializar_componentes(dados_disciplina)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
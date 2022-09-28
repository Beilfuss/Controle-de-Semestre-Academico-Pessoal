import PySimpleGUI as sg

class TelaDisciplina():

    def __init__(self, controlador_disciplina):
        self.__controlador_disciplina = controlador_disciplina
        self.__janela = None
        self.inicializar_componentes()

    def inicializar_componentes(self, dados_disciplinas=[]):
        layout = [
            [sg.Text("CÓDIGO DA DISCIPLINA - NOME DA DISCIPLINA")],
            [sg.Text("Professor: ")],
            [sg.Text("Média Parcial: ")],
            [sg.Text("Faltas Remanescentes: ")],
            [sg.Submit(button_text="Colegas"), sg.Submit(button_text="Registrar Falta")],
            [sg.Text("")],
            [sg.Text("Lista de Atividades")],
            [sg.Text("TABELA")],
            [sg.Submit(button_text="Ver Atividade"), sg.Submit(button_text="Cadastrar Atividade")],
            [sg.Text("")],
            [sg.Text("Aulas")],
            [sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
            [sg.Text("Cadastrar Aula")],
            [sg.Text("Excluir Disciplina"), sg.Text("Alterar Disciplina"), sg.Text("Voltar")]
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
import PySimpleGUI as sg


class TelaDadosDisciplina():

    def __init__(self, controlador_disciplina):
        self.__controlador_disciplina = controlador_disciplina
        self.__janela = None
        self.inicializar_componentes(dados_disciplina={"nome": "", "codigo": "", "professor": "",
                               "numAulas": "", "rec": ""})

    def inicializar_componentes(self, dados_disciplina):
        layout = [
            [sg.Text('Cadastro de Disciplina:')],
            [sg.Text("Nome*"), sg.InputText(dados_disciplina["nome"], key='nome')],
            [sg.Text("Código*"), sg.InputText(dados_disciplina["codigo"], key='codigo')],
            [sg.Text("Professor*"), sg.InputText(dados_disciplina["professor"], key='professor')],
            [sg.Text("Número de aulas*"), sg.InputText(dados_disciplina["numAulas"], key='numAulas')],
            [sg.Text("Recuperação*"), sg.Radio('Sim', "true", default=True, size=(10 ,1)), sg.Radio('Não', "false")],
            [sg.Cancel(button_text="Cancelar"),sg.Submit(button_text="Cadastrar Disciplina")]
        ]
        self.__janela = sg.Window('Dados da Disciplina').Layout(layout)

    def abrir(self, dados_disciplina):
        self.inicializar_componentes(dados_disciplina)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()
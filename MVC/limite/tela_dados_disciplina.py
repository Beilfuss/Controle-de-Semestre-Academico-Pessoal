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
            [sg.Text("Nome*", size=(13, 1)), sg.InputText(dados_disciplina["nome"],
                                                          key='nome', tooltip="Ex.: Análise e Projeto de Sistemas")],
            [sg.Text("Código*", size=(13, 1)), sg.InputText(dados_disciplina["codigo"],
                                                            key='codigo', tooltip="Ex.: INE5608")],
            [sg.Text("Professor*", size=(13, 1)), sg.InputText(
                dados_disciplina["professor"], key='professor', tooltip="Ex.: Fabiane")],
            [sg.Text("Número de aulas*", size=(13, 1)), sg.InputText(
                dados_disciplina["numAulas"], key='numAulas', tooltip="Ex.: 40")],
            [sg.Text("Recuperação*"), sg.Radio('Sim', "RADIO1",
                                               default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
            [sg.Cancel(button_text="Cancelar", button_color="red"),
             sg.Submit(button_text="Confirmar")]
        ]

        if dados_disciplina['rec'] == "Não":
            layout[5] = [sg.Text("Recuperação*"), sg.Radio('Sim', "RADIO1",
                                                           size=(10, 1)), sg.Radio('Não', "RADIO1", default=True)]

        self.__janela = sg.Window('Dados da Disciplina').Layout(layout)

    def abrir(self, dados_disciplina):
        self.inicializar_componentes(dados_disciplina)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()

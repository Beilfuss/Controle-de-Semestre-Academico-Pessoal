import PySimpleGUI as sg


class TelaFaltas():

    def __init__(self, controlador_disciplina):
        self.__controlador_disciplina = controlador_disciplina
        self.__janela = None
        self.inicializar_componentes(dados_faltas={'nome': "", 'faltas': ""})

    def inicializar_componentes(self, dados_faltas):

        layout = [
            [sg.Text('Cadastro de Faltas', font="bold", justification="center", expand_x=True)],

            [sg.Text("{nome}".format(nome=dados_faltas['nome']), justification="center")], # Por que não justifica?
            [sg.Text("")],
            
            [sg.Text("Faltas anteriores")],
            [sg.Table(dados_faltas['faltas'], headings=[
                "Dia", "Quantidade"], key="row_falta_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            
            [sg.Submit(button_text="Excluir Falta", button_color="red")],
            [sg.Text("")],
            [sg.Text("Registrar falta")],

            [sg.Text("Dia* (DD/MM/AAAA)", size=(16, 1)), sg.InputText(key='dia', tooltip="12/12/2022")],
            [sg.Text("Quantidade de aulas*", size=(16, 1)), sg.InputText(key='numFaltas', tooltip="2")],
                      
            [sg.Submit(button_text="Cadastrar Faltas"), sg.Submit(button_text="Voltar")]
        ]

        self.__janela = sg.Window(
            "TelaFaltas", default_element_size=(40, 1)).Layout(layout)

    def abrir(self, dados_faltas):
        self.inicializar_componentes(dados_faltas)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
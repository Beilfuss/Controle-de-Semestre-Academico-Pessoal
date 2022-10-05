import PySimpleGUI as sg

class TelaDadosAtividade():

    def __init__(self, controlador_atividade):
        self.__controlador_atividade = controlador_atividade
        self.__janela = None

    def inicializar_componentes(self):
        layout = [
            [sg.Text('Cadastro de Atividade')],
            [sg.Text("atividade.disciplina.nome")],
            [sg.Text("Nome*", size=(18,0)), sg.InputText("atividade.nome", key="atividade_nome")],
            [sg.Text("Tipo da atividade*", size=(18,0)), sg.Radio("Prova", "tipo_de_atividade", default=True, key="tipo_de_atividade.prova"), sg.Radio("Trabalho", "tipo_de_atividade", key="tipo_de_atividade.trabalho")],
            [sg.Text("Data*", size=(18,0)), sg.InputText("atividade.data", key="atividade_nome")],
            [sg.Text("Peso da nota(em %)*", size=(18,0)), sg.InputText("atividade.peso", key="atividade_peso")],
            [sg.Text("Em grupo*", size=(18,0)), sg.Radio("Sim", "em_grupo", default=True, key="em_grupo.sim"), sg.Radio("Trabalho", "em_grupo", key="em_grupo.nao")],
            [sg.Submit("Confirmar", key="bt_confirmar"), sg.Submit("Cancelar", key="bt_cancelar")]
        ]
        self.__janela = sg.Window("Cadastro de atividade", element_justification="c").Layout(layout)

    def abrir(self):
        self.inicializar_componentes()
        evento, valores = self.__janela.Read()
        print(evento, valores)
        return evento, valores

    def fechar(self):
        self.__janela.Close()
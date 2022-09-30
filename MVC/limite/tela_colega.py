import PySimpleGUI as sg


class TelaColega:

    def __init__(self, controlador_colega):
        self.__controlador_colega = controlador_colega
        self.__janela = None

    def inicializar_componentes(self, dados_colegas):

        dados_display = [(colega["nome"], colega["matricula"])
                         for colega in dados_colegas]

        frame_adicionar_colega = sg.Frame("Adicionar Colega", [
            [sg.Text("Nome*"), sg.InputText("", key="nome")],
            [sg.Text("Matricula*"), sg.InputText("", key="matricula")],
            [sg.Button("Adicionar Colega", key=2)]
        ])

        layout = [
            [sg.Text("Colegas", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Nome da Disciplina", font="bold",
                     justification="center", expand_x=True)],
            [sg.Table(dados_display, headings=[
                "Nome", "Matrícula"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            [sg.Button("Excluir", key=1)],
            [frame_adicionar_colega],
            [sg.Button("Voltar", key=0)]
        ]

        self.__janela = sg.Window("Colegas").Layout(layout)

    def abrir(self, dados_colegas):
        self.inicializar_componentes(dados_colegas)
        botao, valores = self.__janela.Read()
        self.fechar()

        if(botao == sg.WIN_CLOSED or botao == 0):
            self.__janela.Close()
            return (0, {})

        return botao, valores

    def fechar(self):
        self.__janela.Close()

    def mostrar_mensagem(self, mensagem: str):

        layout = [[sg.Text(mensagem)],
                  [sg.Submit(button_text="Ok")]]

        self.__janela = sg.Window("Mensagem").Layout(layout)

        self.__janela.Read()
        self.fechar()

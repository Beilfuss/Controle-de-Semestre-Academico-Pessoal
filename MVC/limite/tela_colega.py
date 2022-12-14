import PySimpleGUI as sg


class TelaColega:

    def __init__(self, controlador_colega):
        self.__controlador_colega = controlador_colega
        self.__janela = None

    def inicializar_componentes(self, nome_disciplina, dados_colegas):

        dados_display = [(colega["nome"], colega["matricula"])
                         for colega in dados_colegas]

        frame_adicionar_colega = sg.Frame("Adicionar Colega", [
            [sg.Text("Nome*", size=(7, 1)), sg.InputText("",
                                                         key="nome", tooltip="Ex.: Matheus")],
            [sg.Text("Matricula*", size=(7, 1)),
             sg.InputText("", key="matricula", tooltip="Ex.: 12345678")],
            [sg.Button("Adicionar Colega", key=2)]
        ])

        layout = [
            [sg.Text("Colegas", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(nome_disciplina, font="bold",
                     justification="center", expand_x=True)],
            [sg.Table(dados_display, headings=[
                "Nome", "Matrícula"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            [sg.Button("Alterar", key=3), sg.Button(
                "Excluir", key=1, button_color="red")],
            [frame_adicionar_colega],
            [sg.Button("Voltar", key=0)]
        ]

        self.__janela = sg.Window("Colegas").Layout(layout)

    def inicializar_alteracao(self, matricula, nome):

        layout = [
            [sg.Text("Alterar Colega", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(matricula, justification="center", expand_x=True)],
            [[sg.Text("Nome*", size=(7, 1)),
              sg.InputText(nome, key="nome")]],
            [sg.Button("Confirmar", key=1), sg.Button("Voltar", key=0)]
        ]

        self.__janela = sg.Window("Colegas").Layout(layout)

    def abrir(self, nome_disciplina, dados_colegas):
        self.inicializar_componentes(nome_disciplina, dados_colegas)
        botao, valores = self.__janela.Read()
        self.fechar()

        if (botao == sg.WIN_CLOSED or botao == 0):
            self.__janela.Close()
            return (0, {})

        return botao, valores

    def abrir_alteracao(self, matricula, nome):
        self.inicializar_alteracao(matricula, nome)
        botao, valores = self.__janela.Read()
        self.fechar()

        if (botao == sg.WIN_CLOSED or botao == 0):
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

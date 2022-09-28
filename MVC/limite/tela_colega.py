import PySimpleGUI as sg


class TelaColega:

    def __init__(self, controlador_colega):
        self.__controlador_colega = controlador_colega
        self.__janela = None

    def inicializar_componentes(self, dados_colegas):

        layout = [
            [sg.Text("Colegas")],
            [sg.Text("Nome da Disciplina")],
            [sg.Table(dados_colegas, headings=[
                "Nome"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            [sg.Button("Excluir", key=1)],
            [sg.Text("Nome*"), sg.InputText("", key="nome")],
            [sg.Button("Voltar", key=0),
             sg.Button("Adicionar Colega", key=2)]
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

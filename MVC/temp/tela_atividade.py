import PySimpleGUI as sg


class TelaAtividade():

    def __init__(self):

        self.__janela = None

    def inicializar_componentes(self, disciplina_nome, dados_display=[]):

        layout = [
            [sg.Text("Atividade 1", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(disciplina_nome, font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Dados da disciplina")],
            [sg.Text("Grupo", font="bold",
                     justification="center", expand_x=True)],
            [sg.Table(dados_display, headings=[
                "Nome", "Matricula"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            [sg.Button("Criar/Alterar Grupo", key=1)],
            [sg.Button("Voltar", key=0)]
        ]

        self.__janela = sg.Window("Colegas").Layout(layout)

    def abrir(self, disciplina_nome, dados_display=[]):
        self.inicializar_componentes(disciplina_nome, dados_display)
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

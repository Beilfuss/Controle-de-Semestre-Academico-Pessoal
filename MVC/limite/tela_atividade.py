import PySimpleGUI as sg


class TelaAtividade:

    def __init__(self, controlador_atividade):
        self.__controlador_atividade = controlador_atividade
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

    def inicializar_cadastro(self, nome_disciplina):

        layout = [
            [sg.Text("Cadastro de Atividade", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(nome_disciplina, font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Nome*", size=(7, 1)), sg.InputText("",
                                                         key="nome", tooltip="Ex.: T1 - Diagrama de Classes")],
            [sg.Text("Tipo de Atividade*"), sg.Radio('Prova', "tipo_atividade",
                                                     default=True, size=(10, 1)), sg.Radio('Trabalho', "tipo_atividade")],
            [sg.Text("Data*", size=(7, 1)), sg.InputText("",
                                                         key="data", tooltip="Ex.: T1 - Diagrama de Classes")],
            [sg.Text("Peso da nota (%)*", size=(7, 1)), sg.InputText("",
                                                                     key="peso", tooltip="Ex.: T1 - Diagrama de Classes")],
            [sg.Checkbox("Em grupo", default=False, key="grupo"), sg.Checkbox(
                "Priorizar", default=False, key="priorizar")],
            [sg.Button("Cancelar", key="cancelar", button_color="red"), sg.Button(
                "Confirmar", key=2)],
        ]

        self.__janela = sg.Window("Cadastrar Atividade").Layout(layout)

    def abrir_cadastro(self, nome_disciplina):
        self.inicializar_cadastro(nome_disciplina)
        botao, valores = self.__janela.Read()
        self.fechar()

        if (botao == sg.WIN_CLOSED or botao == "cancelar"):
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

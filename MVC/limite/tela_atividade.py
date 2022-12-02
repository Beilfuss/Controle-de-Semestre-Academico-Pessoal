import PySimpleGUI as sg


class TelaAtividade:

    def __init__(self, controlador_atividade):
        self.__controlador_atividade = controlador_atividade
        self.__janela = None

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

        print(botao)
        if (botao == sg.WIN_CLOSED or botao == "cancelar"):
            self.__janela.Close()
            return (0, {})

        return botao, valores

    def fechar(self):
        self.__janela.Close()

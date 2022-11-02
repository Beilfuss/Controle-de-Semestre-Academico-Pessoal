import PySimpleGUI as sg


class TelaGrupo:

    def __init__(self, controlador_grupo):
        self.__controlador_grupo = controlador_grupo
        self.__janela = None

    def inicializar_componentes(self, nome_disciplina, colegas_dados=[], membros_dados=[]):

        layout = [
            [sg.Text("Cadastro de Grupo", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(nome_disciplina, font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Número de Membros*", size=(13, 1)), sg.InputText(2,
                                                                       key='numColegas', tooltip="Ex.: 3")],
            [sg.Text("Colegas da Disciplina", font="bold",
                     justification="center", expand_x=True)],
            [sg.Table(colegas_dados, headings=[
                "Nome", "Matrícula"], key="novo_colega_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=5, expand_x=True)],
            [sg.Button("Adicionar Colega", key=1)],
            [sg.Text("Membros do Grupo", font="bold",
                     justification="center", expand_x=True)],
            [sg.Table(membros_dados, headings=[
                "Nome"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            [sg.Button("Excluir Colega", key=2)],
            [sg.Button("Cancelar", key=0), sg.Button("Confirmar", key=3)]
        ]

        self.__janela = sg.Window("Cadastro de Grupo").Layout(layout)

    def abrir(self, nome_disciplina, colegas_dados):
        self.inicializar_componentes(nome_disciplina, colegas_dados)
        botao, valores = self.__janela.Read()
        self.fechar()

        if (botao == sg.WIN_CLOSED or botao == 0):
            self.__janela.Close()
            return (0, {})

        return botao, valores

    def fechar(self):
        self.__janela.Close()

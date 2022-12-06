import PySimpleGUI as sg


class TelaAtividade:

    def __init__(self, controlador_atividade):
        self.__controlador_atividade = controlador_atividade
        self.__janela = None

    def inicializar_componentes(self, disciplina_nome, colegas_display, dados_atividade):

        priorizar_button_text = "Priorizar" if not dados_atividade[
            "priorizar"] else "Remover Prioridade"

        grupo_display = [[sg.Text("Grupo", font="bold", justification="center", expand_x=True)],
                         [sg.Table(colegas_display, headings=["Nome", "Matricula"], key="row_index",
                                   select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
                         [sg.Button("Criar/Alterar Grupo", key=1)]] if dados_atividade["temGrupo"] else [sg.Text("")]

        layout = [
            [sg.Text(dados_atividade["nome"], font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(disciplina_nome, font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Tipo: {tipo}".format(
                tipo=dados_atividade['tipo']))],
            [sg.Text("Data de Entrega: {data}".format(
                data=dados_atividade['data']))],
            [sg.Text("Peso: {peso}%".format(
                peso=dados_atividade['peso_nota']))],
            [sg.Text("Nota: -")],
            [sg.Text("Grupo: {grupo}".format(
                grupo="Sim" if dados_atividade['temGrupo'] else "Não"))],
            [sg.Text("Prioridade: {grupo}".format(
                grupo="Sim" if dados_atividade['priorizar'] else "Não"))],
            [sg.Button("Alterar Nota", key=5), sg.Button(
                priorizar_button_text, key=2)],
            grupo_display,
            [sg.Button("Excluir Atividade", key=3, button_color="red"),
             sg.Button("Alterar Atividade", key=4), sg.Button("Voltar", key=0)]
        ]

        self.__janela = sg.Window("Colegas").Layout(layout)

    def abrir(self, disciplina_nome, colegas_display=[], dados_atividade={}):
        self.inicializar_componentes(
            disciplina_nome, colegas_display, dados_atividade)
        botao, valores = self.__janela.Read()
        self.fechar()

        if (botao == sg.WIN_CLOSED or botao == 0):
            self.__janela.Close()
            return (0, {})

        return botao, valores

    def inicializar_cadastro(self, nome_disciplina, dados_atividade, alterar=False):

        layout = [
            [sg.Text("Cadastro de Atividade" if not alterar else "Alteração de Atividade", font="bold",
                     justification="center", expand_x=True)],
            [sg.Text(nome_disciplina, font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Nome*", size=(7, 1)), sg.InputText(dados_atividade["nome"],
                                                         key="nome", tooltip="Ex.: T1 - Diagrama de Classes")],
            [sg.Text("Tipo de Atividade*"),
             sg.Radio('Prova', "tipo_atividade",
             disabled=alterar,
                      default=dados_atividade["tipo"] != "Trabalho", size=(10, 1)),
             sg.Radio('Trabalho', "tipo_atividade", disabled=alterar, default=dados_atividade["tipo"] == "Trabalho")],
            [sg.Text("Data*", size=(7, 1)), sg.InputText(dados_atividade["data"],
                                                         key="data", tooltip="Ex.: T1 - Diagrama de Classes")],
            [sg.Text("Peso da nota (%)*", size=(7, 1)), sg.InputText(dados_atividade["peso_nota"],
                                                                     key="peso", tooltip="Ex.: T1 - Diagrama de Classes")],
            [sg.Checkbox("Em grupo", default=dados_atividade["temGrupo"], key="grupo"), sg.Checkbox(
                "Priorizar", default=dados_atividade["priorizar"], key="priorizar")],
            [sg.Button("Cancelar", key="cancelar", button_color="red"), sg.Button(
                "Confirmar", key=2)],
        ]

        self.__janela = sg.Window("Cadastrar Atividade").Layout(layout)

    def abrir_cadastro(self, nome_disciplina, dados_atividade={"nome": "",
                                                               "tipo": "",
                                                               "data": "",
                                                               "peso_nota": "",
                                                               "temGrupo": False,
                                                               "priorizar": False}, alterar=False):
        self.inicializar_cadastro(
            nome_disciplina, dados_atividade, alterar)
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

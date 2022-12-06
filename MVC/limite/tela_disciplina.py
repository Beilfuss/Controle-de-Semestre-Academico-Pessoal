import PySimpleGUI as sg


class TelaDisciplina():

    def __init__(self, controlador_disciplina):
        self.__controlador_disciplina = controlador_disciplina
        self.__janela = None
        self.inicializar_componentes()

    def inicializar_componentes(self, dados_disciplinas=None, atividades_dados=[], alerta_peso=False):

        if dados_disciplinas is None:
            dados_disciplinas = {'nome': '', 'codigo': '', 'professor': '', 'numAulas': '',
                                 0: '', 1: '', 'rec': ''}

        alerta_peso_display = [sg.Text(
            "Atenção! Peso total das notas é diferente de 100%. Verifique as atividades" if alerta_peso else "", text_color="red")]

        atividades_dados_display = [(atividade["nome"], atividade["data"], atividade["tipo"],  str(atividade["peso_nota"])+"%",  "Sim" if atividade["temGrupo"] else "Não", "-")
                                    for atividade in atividades_dados]

        layout = [
            [sg.Text("{codigo} - {nome}".format(codigo=dados_disciplinas['codigo'], nome=dados_disciplinas['nome']), font="bold",
                     justification="center", expand_x=True)],
            [sg.Text("Professor: {professor}".format(
                professor=dados_disciplinas['professor']))],
            [sg.Text("Recuperação: {rec}".format(
                rec=dados_disciplinas['rec']))],
            [sg.Text("Média Parcial: ")],
            [sg.Text("Faltas Remanescentes: ")],
            [sg.Submit(button_text="Encerrar Disciplina", button_color="red"), sg.Submit(
                button_text="Colegas"), sg.Submit(button_text="Registrar Falta")],
            [sg.Text("")],
            [sg.Text("Lista de Atividades")],
            alerta_peso_display,
            [sg.Table(atividades_dados_display, headings=[
                "Nome", "Data de Entrega", "Tipo", "Peso", "Grupo", "Prioridade"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE, justification="left", num_rows=8, expand_x=True)],
            [sg.Submit(button_text="Ver Atividade"), sg.Submit(
                button_text="Cadastrar Atividade")],
            [sg.Text("")],
            [sg.Text("Aulas")],
            [sg.Table([['Segunda-Feira', '20h20', 'CTC304'], ['Quarta-Feira',
                      '20h20', 'CTC204']], ['Dia', 'Hora', 'Sala'], num_rows=2)],
            [sg.Submit(button_text="Cadastrar Aula")],
            [sg.Submit(button_text="Excluir Disciplina", button_color="red"), sg.Submit(button_text="Alterar Disciplina"),
             sg.Submit(button_text="Voltar")]
        ]

        self.__janela = sg.Window(
            "TelaDisciplina", default_element_size=(40, 1)).Layout(layout)

    def abrir(self, dados_disciplina=[], atividades_dados=[], alerta_peso=False):
        self.inicializar_componentes(
            dados_disciplina, atividades_dados, alerta_peso)
        botao, valores = self.__janela.Read()
        return botao, valores

    def fechar(self):
        self.__janela.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

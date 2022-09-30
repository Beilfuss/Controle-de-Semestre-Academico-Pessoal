from limite.tela_dados_disciplina import TelaDadosDisciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina
from dao.disciplina_dao import DisciplinaDAO


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)
        self.__dao = DisciplinaDAO()  # ARMAZENAR DISCIPLINAS, TROCAR DEPOIS

    def obter_dados_disciplinas(self):
        return [disciplina.desempacotar() for disciplina in self.__dao.buscar_todos()]

    def abrir_tela_disciplina(self, dados_disciplina):

        botao, valores = self.__tela_disciplina.abrir(dados_disciplina)
        
        if botao == "Voltar":
            self.__tela_disciplina.fechar()
        elif botao == "Alterar Disciplina":
            self.alterar_disciplina(dados_disciplina)

    def incluir_disciplina(self, values=None):

        while True:
            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(
                dados_disciplina={"nome": "", "codigo": "", "professor": "",
                                  "numAulas": "", "rec": ""})

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break

            try:
                int(dados_disciplina["numAulas"])
                if dados_disciplina == {"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "rec": ""
                        } or (dados_disciplina["nome"]).isdigit() or (dados_disciplina["professor"]).isdigit() or \
                        (dados_disciplina["numAulas"]).isalpha():
                    raise ValueError
                    # VERIFICAR SE A DISCIPLINA JÁ EXISTE

                if dados_disciplina[0]:
                    dados_disciplina["rec"] = 1 # Tem REC
                else:
                    dados_disciplina["rec"] = 0 # Não tem REC
                
                sucesso = self.__dao.persist_disciplina(dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                                        dados_disciplina["numAulas"], dados_disciplina["rec"], None, None, None, None)
                
                if not sucesso:
                    self.__tela_disciplina.mostrar_mensagem("Atenção", "Disciplina já cadastrada!")

                break

            except ValueError:
                self.__tela_disciplina.mostrar_mensagem(
                    "Atenção", "Dados inválidos. Tente novamente!")
                continue
    
    def alterar_disciplina(self, dados_disciplina):
        print('Dados disciplina: ', dados_disciplina)
        while True:
            botao, dados_disciplina = self.__tela_dados_disciplina.abrir(dados_disciplina)

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break

            try:
                int(dados_disciplina["numAulas"])
                if dados_disciplina == {"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "rec": ""
                        } or (dados_disciplina["nome"]).isdigit() or (dados_disciplina["professor"]).isdigit() or \
                        (dados_disciplina["numAulas"]).isalpha():
                    raise ValueError
                    # VERIFICAR SE A DISCIPLINA JÁ EXISTE

                if dados_disciplina[0]:
                    dados_disciplina["rec"] = 1 # Tem REC
                else:
                    dados_disciplina["rec"] = 0 # Não tem REC
                
                sucesso = self.__dao.persist_disciplina(dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                                        dados_disciplina["numAulas"], dados_disciplina["rec"], None, None, None, None)
                
                if not sucesso:
                    self.__tela_disciplina.mostrar_mensagem("Atenção", "Disciplina já cadastrada!")
                
                break

            except ValueError:
                self.__tela_disciplina.mostrar_mensagem(
                    "Atenção", "Dados inválidos. Tente novamente!")
                continue

    def excluir_disciplina(self):
        '''
        Por enquanto você está usando código como identificador único, que deverá mudar para id posteriormente.
        Os seguintes passos devem funcionar com código e provavelmente quando trocar com id, mas podem ser necessárias adaptações
        - Passo 1: método excluir_disciplina deverá receber o código/id da disciplina como argumento. Fácil de fazer, pois o método abrir tela recebe os dados da disciplina, que incluem o código e incluirão o id
        - Passo 2: chamar o método delete disciplina do DAO, passando o código da disciplina como argumento em vez de um index. Trocar o nome do argumento para representar corretamente
        - Passo 3: excluir a linha disciplina = list(... etc, não será necessária
        - Passo 4: Corrigir a query conforme o nome da tabela. Utilizar o codigo/id da disciplina com parâmetro
        - Passo 5: Excluir a disciplina do cache, usando o codigo/id como argumento do pop
        '''
        pass

    def listar_disciplinas(self):
        pass
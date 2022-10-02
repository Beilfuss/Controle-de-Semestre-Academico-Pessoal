from limite.tela_dados_disciplina import TelaDadosDisciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina
from dao.disciplina_dao import DisciplinaDAO
from excecoes.jaExistenteException import JaExistenteException


class ControladorDisciplina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_disciplina = TelaDisciplina(self)
        self.__tela_dados_disciplina = TelaDadosDisciplina(self)
        self.__dao = DisciplinaDAO()

    def listar_disciplinas(self):
        return [disciplina.desempacotar() for disciplina in self.__dao.buscar_todos()]

    def abrir_tela_disciplina(self, dados_disciplina):


        #opcoes = {
        #"Voltar": self.__tela_dados_disciplina.fechar,
        #"Alterar Disciplina": self.alterar_disciplina,
        #"Excluir Disciplina": self.excluir_disciplina
        #}
        

        botao, valores = self.__tela_disciplina.abrir(dados_disciplina)
        
        #self.__tela_dados_disciplina.fechar()
#
        #if(botao != "Voltar"):
        #    opcoes[botao](dados_disciplina)

        if botao == "Voltar":
            self.__tela_disciplina.fechar()
        elif botao == "Alterar Disciplina":
            self.__tela_disciplina.fechar()
            self.alterar_disciplina(dados_disciplina)
        elif botao == "Excluir Disciplina":
            self.__tela_disciplina.fechar()
            self.excluir_disciplina(dados_disciplina["id"])


    def incluir_disciplina(self, dados_disciplina=None): 
        
        alteracao = False

        while True:

            '''
                Troquei dados_disciplina != None por dados_disciplina is not None, conforme pep8:

                https://peps.python.org/pep-0008/

                Comparisons to singletons like None should always be done with is or is not, never the equality operators.

                Also, beware of writing if x when you really mean if x is not None – e.g. when testing whether a variable or argument that 
                defaults to None was set to some other value. The other value might have a type (such as a container) that could be false 
                in a boolean context!
            
            '''
            if dados_disciplina is not None:
                alteracao = True
                dados_disciplina_old = dados_disciplina
                botao, dados_disciplina = self.__tela_dados_disciplina.abrir(dados_disciplina)


            else:
                botao, dados_disciplina = self.__tela_dados_disciplina.abrir(
                dados_disciplina={"nome": "", "codigo": "", "professor": "",
                                  "numAulas": "", "rec": ""})

            self.__tela_dados_disciplina.fechar()

            if botao == "Cancelar":
                break

            try:
                dados_disciplina['numAulas'] = int(dados_disciplina["numAulas"])

                if dados_disciplina == {"nome": "", "codigo": "", "professor": "", "numero_aulas": "", "rec": ""
                        } or (dados_disciplina["nome"]).isdigit() or (dados_disciplina["professor"]).isdigit():
                    raise ValueError

                disciplinas = self.__dao.buscar_todos()
                for disciplina in disciplinas:
                    #Nome da disciplina é um bom critério para decidir se a disciplina já existe ou não?
                    if disciplina.nome == dados_disciplina['nome']:
                        raise JaExistenteException

                if dados_disciplina[0]:
                    dados_disciplina["rec"] = "Sim" # Tem REC
                else:
                    dados_disciplina["rec"] = "Não" # Não tem REC
                
                #retirados os argumentos none em conformidade com a assinatura do método alterado. Os dados aulas, colegas, atividades, etc, nunca serão 
                #conhecidos ou informados na tela de cadastro/alteração, logo acredito que não precisam estar aqui como argumentos
                sucesso = self.__dao.persist_disciplina(dados_disciplina["nome"], dados_disciplina["codigo"], dados_disciplina["professor"],
                                        dados_disciplina["numAulas"], dados_disciplina["rec"])
                
                if not sucesso:
                    self.__tela_disciplina.mostrar_mensagem("Atenção", "Disciplina já cadastrada!")

                if alteracao == True:
                    return dados_disciplina

                break

            except ValueError:
                self.__tela_disciplina.mostrar_mensagem(
                    "Atenção", "Dados inválidos. Tente novamente!")
                continue
            except JaExistenteException:
                dados_disciplina = dados_disciplina_old
                self.__tela_disciplina.mostrar_mensagem('Atenção', 'Disciplina já existente, tente novamente!')
    
    def alterar_disciplina(self, dados_disciplina):

        #usar update para fazer a alteração da disciplina
        dados_disciplina_old = dados_disciplina
        dados_disciplina = self.incluir_disciplina(dados_disciplina)

        #alterado != None para is not None conforme comentário anterior
        if dados_disciplina is not None:
            if dados_disciplina['codigo'] != dados_disciplina_old['codigo']:
                self.excluir_disciplina(dados_disciplina_old['codigo'])
            
    def excluir_disciplina(self, id):
        self.__dao.delete_disciplina(id)

        '''
        Por enquanto você está usando código como identificador único, que deverá mudar para id posteriormente.
        Os seguintes passos devem funcionar com código e provavelmente quando trocar com id, mas podem ser necessárias adaptações
        - Passo 1: método excluir_disciplina deverá receber o código/id da disciplina como argumento. Fácil de fazer, pois o método abrir tela recebe os dados da disciplina, que incluem o código e incluirão o id
        - Passo 2: chamar o método delete disciplina do DAO, passando o código da disciplina como argumento em vez de um index. Trocar o nome do argumento para representar corretamente
        - Passo 3: excluir a linha disciplina = list(... etc, não será necessária
        - Passo 4: Corrigir a query conforme o nome da tabela. Utilizar o codigo/id da disciplina com parâmetro
        - Passo 5: Excluir a disciplina do cache, usando o codigo/id como argumento do pop
        '''

                
    def incluir_colega(self, disciplina_id, colega):
        
        '''
        sucesso = self.__dao.incluir_colega(disciplina_id, colega)

        if(not sucesso):
            self.__tela.mostrar_mensagem("Colega já cadastrado!")


        no dao:
        CREATE TABLE IF NOT EXISTS COLEGAS_DISCIPLINAS(disciplina_id INTEGER NOT NULL, colega_id INTEGER NOT NULL, FOREIGN KEY(disciplinas_id) REFERENCES DISCIPLINAS(id), FOREIGN KEY(colega_id) REFERENCES COLEGAS(id))																
        
        def incluir_colega(self, disciplina_id, colega):

            try:
                query = "INSERT INTO COLEGAS_DISCIPLINAS(disciplina_id, colega_id) VALUES(?, ?)"
                query_params = (disciplina_id, colega_id)

                self.executar_query(query, query_params)

                self._cache[disciplina_id].colegas.push(colega)
                return True
            except Exception:
                return False

        '''
        pass
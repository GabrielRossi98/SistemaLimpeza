from src.model.DAO.base_db import BaseDB



class Funcionario_DAO:

    def __init__(self):
        self.__conn=BaseDB("funcionario.json")

    def addFuncionario(self,data:dict):
        try:
            self.__conn.salve(data)
            return "Funcionario salvo com sucesso !"
        except Exception as e:
            raise ValueError("Erro no momento de salvar o funcionario no banco de dados",e)


    def lerFuncionario(self):
        return self.__conn.readList()

    def deletarFuncionario(self,id_funcionario):
        novo_funcionario=[funcionario for funcionario in self.lerFuncionario() if funcionario["id"]!=id_funcionario]
        if len(novo_funcionario)==len(self.lerFuncionario()):
            raise ValueError("Nenhum Funcionário encontrado com esse ID")

        self.__conn.salveList(novo_funcionario)
        print("Deletado com sucesso!")

    def buscarPorID(self,id):
        try:
            funcionarioEncontrado=[funcionario for funcionario in self.lerFuncionario()if funcionario["id"]==id][0]
            return funcionarioEncontrado
        except IndexError as e:
            raise ValueError("Produto não existe no sistema",e)
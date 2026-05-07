from src.model.DAO.base_db import BaseDB


class Fornecedor_DAO:

    def __init__(self):
        self.__conn=BaseDB("fornecedor.json")

    def addFornecedor(self,data:dict):
        try:
            self.__conn.salve(data)
            return "Fornecedor salvo com sucesso !"
        except Exception as e:
            raise ValueError("Erro no momento de salvar o fornecedor no banco de dados",e)


    def lerFornecedor(self):
        return self.__conn.readList()

    def deletarFornecedor(self,id_fornecedor):
        novo_fornecedor=[fornecedor for fornecedor in self.lerFornecedor() if fornecedor["id"]!=id_fornecedor]
        if len(novo_fornecedor)==len(self.lerFornecedor()):
            raise ValueError("Nenhum Fornecedor encontrado com esse ID")

        self.__conn.salveList(novo_fornecedor)
        print("Deletado com sucesso!")

    def buscarPorID(self,id):
        try:
            fornecedorEncontrado=[fornecedor for fornecedor in self.lerFornecedor()if fornecedor["id"]==id][0]
            return fornecedorEncontrado
        except IndexError as e:
            raise ValueError("Produto não existe no sistema",e)
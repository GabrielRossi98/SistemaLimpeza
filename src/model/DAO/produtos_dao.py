from src.model.DAO.base_db import BaseDB

class Produtos_DAO:

    def __init__(self):
        self.__conn=BaseDB("produtos.json")

    def addProdutos(self,data:dict):
        try:
            self.__conn.salve(data)
            return "Produto salvo com sucesso !"
        except Exception:
            raise ValueError("Não foi possivel salvar o produto")


    def lerProdutos(self):
        return self.__conn.readList()

    def deletarProduto(self,id_produto):
        nova_lista=[produto for produto in self.lerProdutos() if produto["id"]!=id_produto]
        if len(nova_lista)==len(self.lerProdutos()):
            raise ValueError("Nenhum Produto encontrado com esse ID")

        self.__conn.salveList(nova_lista)
        print("Deletado com sucesso!")

    def buscarPorID(self,id):
        try:
            produtoEncontrado=[produto for produto in self.lerProdutos()if produto["id"]==id][0]
            return produtoEncontrado
        except IndexError as e:
            raise ValueError("Produto não existe no sistema",e)


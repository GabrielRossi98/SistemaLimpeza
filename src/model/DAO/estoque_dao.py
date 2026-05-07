
from src.model.DAO.base_db import BaseDB

class Estoque(BaseDB):
    def __init__(self):
        super().__init__("estoque.json")

    def lerEstoqueTodo(self):
        return self.readList()

    def addNovoProdutoEstoque(self,data):
        self.salve(data)
        print("Add com sucesso o produto no estoque")

    def incrementarProduto(self,id_produto,quantidade:int):
        linha,produto=[(index,produto) for index, produto in enumerate (self.lerEstoqueTodo())if produto["id"]==id_produto][0]
        produto["quantidade"]+=quantidade
        novaLista=self.lerEstoqueTodo()[linha]=produto
        novaLista[linha]=produto
        self.salveList(novaLista)

    def decrementarProduto(self,id_produto,quantidade:int):
        linha,produto=[(index,produto) for index, produto in enumerate (self.lerEstoqueTodo())if produto["id"]==id_produto][0]
        produto["quantidade"]-=quantidade
        novaLista=self.lerEstoqueTodo()[linha]=produto
        novaLista[linha]=produto
        self.salveList(novaLista)

    def buscarPorID(self,id):
        try:
            produtoEncontrado=[produto for produto in self.lerProdutos()if produto["id"]==id][0]
            return produtoEncontrado
        except IndexError as e:
            raise ValueError("Produto não existe no sistema",e)


if __name__ == '__main__':
    estoque=Estoque()
    # produto= {
    #     "id":2,
    #     "quantidade":0
    # }
    # estoque.addNovoProdutoEstoque(produto)
    estoque.incluirProduto(2,15)
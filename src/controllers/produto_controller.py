from src.infrastructure.services.geradorID import GeradorID
from src.model.entitys.produto import Produto
from src.model.DAO.produtos_dao import Produtos_DAO
class ProdutoController:

    def __init__(self):
        self.dao=Produtos_DAO()


    def cadastrarProduto(self,nome:str,marca:str,valor:float,id_fornecedor:int):
        id_produto: int=GeradorID("produtos.json","id").id_gerado

        p=Produto(id_produto,nome,marca,id_fornecedor,valor)
        self.dao.addProdutos(p.produtoDict())

    def listarProduto(self)->list:
        return self.dao.lerProdutos()

    def buscarProdutoID(self,id:int):
        try:
            return self.dao.buscarPorID(id)
        except Exception as e:
            return e



if __name__ == '__main__':
    p=ProdutoController()
    # p.cadastrarProduto("Feijão","Jeremias",10,1)
    print(p.buscarProdutoID(2))
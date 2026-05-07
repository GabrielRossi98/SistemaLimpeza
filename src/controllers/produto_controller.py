from src.infrastructure.services.geradorID import GeradorID
from src.model.entitys.produto import Produto
from src.model.DAO.produtos_dao import Produtos_DAO
from src.views.produto_view import ProdutoView

class ProdutoController:

    def __init__(self,page,tela:ProdutoView):
        self.dao=Produtos_DAO()
        self.page=page
        tela.btnCadastrarProduto.on_click=self.handleAddproduto
        self.tela=tela



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

    def handleAddproduto(self):
        Produto(GeradorID("produto.json","id").id_gerado,
                self.tela.nomeProduto.value,
                self.tela.marcaProduto.value,
                self.tela.valorProduto.value)




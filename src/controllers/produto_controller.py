from src.infrastructure.services.geradorID import GeradorID
from src.model.entitys.produto import Produto
from src.model.DAO.produtos_dao import Produtos_DAO
from src.views.produto_view import ProdutoView
from flet import *
class ProdutoController:

    def __init__(self,page,tela:ProdutoView):
        self.dao=Produtos_DAO()
        self.page=page
        tela.btnCadastrarProduto.on_click=self.handleAddproduto
        self.tela=tela
        self.listarProduto()


    def listarProduto(self)->None:
        self.tela.tabelaProduto.rows.clear()
        for produto in self.dao.lerProdutos():
            linha=DataRow(
                    cells=[
                        DataCell(Text(produto["id"])),
                        DataCell(Text(produto["nome"])),
                        DataCell(Text(produto["marca"])),
                        DataCell(Text(produto["valor"]))
                    ]
            )
            self.tela.tabelaProduto.rows.append(linha)
        self.page.update()

    def buscarProdutoID(self,id:int):
        try:
            return self.dao.buscarPorID(id)
        except Exception as e:
            return e

    def handleAddproduto(self):

        p=Produto(GeradorID("produtos.json","id").id_gerado,
                self.tela.nomeProduto.value,
                self.tela.marcaProduto.value,
                self.tela.valorProduto.value)
        try:
            self.dao.addProdutos(p.produtoDict())

            self.tela.nomeProduto.value=""
            self.tela.marcaProduto.value=""
            self.tela.valorProduto.value=""

            self.tela.nomeProduto.update()
            self.tela.marcaProduto.update()
            self.tela.valorProduto.update()

            self.listarProduto()


        except Exception as e:
            print(e)




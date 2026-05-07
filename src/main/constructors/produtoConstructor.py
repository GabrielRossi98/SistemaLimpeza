from src.views.produto_view import ProdutoView
from src.controllers.produto_controller import ProdutoController
def ProdutoConstructor(page):
    viewProduto=ProdutoView()
    produtoController=ProdutoController(page,viewProduto)


    return viewProduto
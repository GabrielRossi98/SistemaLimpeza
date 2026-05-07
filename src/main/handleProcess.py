from flet import *
from src.main.constructors.produtoConstructor import ProdutoConstructor

def app(page:Page):
    page.title="Controle de Produto"

    def changeRoutes():
        page.views.clear()
        page.views.append(
            ProdutoConstructor(page)
        )

        page.update()
    page.on_route_change=changeRoutes
    changeRoutes()
from flet import *

class ProdutoView(View):

    def __init__(self):
        super().__init__()
        self.nomeProduto=TextField(label="Nome",icon=Icons.PERSON,col=7)
        self.marcaProduto=TextField(label="Nome", icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.valorProduto=TextField(label="Valor",prefix="R$",col=3)
        self.btnCadastrarProduto=Button("Add Produto",icon=CupertinoIcons.PLUS,col=3)
        self.nomeFornecedor=TextField(label="Nome Fornecedor", icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.btnCadastrarFornecedor = Button("Add Fornecedor", icon=CupertinoIcons.PLUS, col=3)
        self.route="/"

    def build(self):
        modalProduto=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nomeProduto,self.valorProduto
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    ResponsiveRow(
                        controls=[
                            self.marcaProduto, self.btnCadastrarProduto
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )
                ]
            ),
            col={"sm":12,"md":6},
            border=Border.all(4,"#E9EEF6"),
            padding=10,
            height=150
        )

        modalFornecedor = Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nomeFornecedor, self.btnCadastrarFornecedor
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )

                ]
            ),
            col={"sm": 12, "md": 6},
            border=Border.all(4, "#E9EEF6"),
            padding=10,
            height=150
        )

        self.controls=[
            ResponsiveRow(
                controls=[modalProduto,modalFornecedor],
                alignment=MainAxisAlignment.CENTER
            )
        ]
        return self.controls
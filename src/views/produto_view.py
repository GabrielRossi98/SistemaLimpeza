from flet import *

class ProdutoView(View):

    def __init__(self):
        super().__init__()
        self.nomeProduto=TextField(label="Nome",icon=Icons.PERSON,col=7)
        self.marcaProduto=TextField(label="Marca", icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.valorProduto=TextField(label="Valor",prefix="R$",col=3)
        self.btnCadastrarProduto=Button("Add Produto",icon=CupertinoIcons.PLUS,col=3)
        self.route="/"

        self.tabelaProduto=DataTable(
                columns=[
                    DataColumn(label=Text("id")),
                    DataColumn(label=Text("Nome")),
                    DataColumn(label=Text("Marca")),
                    DataColumn(label=Text("Valor R$"))
                ],
                col=12
            )


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
            col=12,
            border=Border.all(4,"#E9EEF6"),
            padding=10,
            height=150
        )

        modalTabela=Container(
            content=ResponsiveRow(
                controls=[self.tabelaProduto],
                alignment=MainAxisAlignment.CENTER
            ),
            padding=Padding(10,20,10,20)
        )



        self.controls=[Column(
            controls=[modalProduto,modalTabela]
            )

        ]
        return self.controls
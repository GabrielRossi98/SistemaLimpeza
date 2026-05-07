from datetime import datetime as dt
class Movimentacao:

    def __init__(self,id_funcionario,dataMovimento:dt=dt.today()):
        self.__dataMovimento=dataMovimento
        self.__id_funcionario=id_funcionario
        self.__id_produto=None
        self.__n_sala=None
        self.__quantidade=None

    def entarEstoque(self,id_produto,quantidade):
        self.__id_produto=id_produto
        self.__quantidade=quantidade

    def saidaEstoque(self,id_produto,quantidade,sala):
        self.__id_produto = id_produto
        self.__quantidade = quantidade
        self.__n_sala=sala

    def movimento(self):
        return {
            "dataMovimento":self.__dataMovimento,
            "id_Funcionario":self.__id_funcionario,
            "id_produto":self.__id_produto,
            "n_sala":self.__n_sala,
            "quantidade":self.__quantidade
                    }
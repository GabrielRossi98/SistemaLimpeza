
class Sala:

    def __init__(self,n_sala:int,andar:int):
        self.__n_sala=n_sala
        self.__andar=andar

    @property
    def sala(self):
        return self.__n_sala

    @property
    def andar(self):
        return self.__andar

    def __eq__(self, other):
        return self.__n_sala==other.__n_sala

    def sala(self):
        return{
            "n_sala":self.__n_sala,
            "andar":self.__andar
        }
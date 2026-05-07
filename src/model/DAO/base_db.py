import json
from json import JSONDecodeError


class BaseDB:

    def __init__(self, file_db:str):
        self.__path=fr"C:\Users\gabriel.rrossi2\PycharmProjects\SistemaLimpeza\src\infrastructure\database\{file_db}"
        self.__file_db=file_db

    def readList(self)-> list:
        try:
            with open(self.__path,"r+",encoding="utf-8") as file:
                return json.load(file)
        except JSONDecodeError:
            return []
        except:
            raise ValueError("Erro ao abrir no arquivo:", self.__file_db)

    def salve(self,data):
        list_data_base=self.readList()
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                list_data_base.append(data)
                json.dump(list_data_base,file,ensure_ascii=False,indent=4)
                print("Salvo com sucesso no banco de dados !")
        except:
            raise ValueError("Erro ao salvar no arquivo:", self.__file_db)

    def salveList(self,lista):
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                json.dump(lista,file,ensure_ascii=False,indent=4)
                print("Salvo com sucesso no banco de dados !")
        except:
            raise ValueError("Erro ao salvar no arquivo:", self.__file_db)
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from datetime import *
import Crawler

class DataBase:

    def __init__(self): #construtor
        
        load_dotenv()
        self.offers = self.connect()

    def connect(self): #conectando ao banco de dados

        client = MongoClient(os.getenv('DB_URI'))
        datab = client['curso']
        return datab.offers 
    
    def insert(self,data: dict): #insercao 
        
        query = {'datenow' : data['datenow']}
        result = self.offers.find_one(query)

        if result is not None:
            print("Dados ja adicionados")
        else:
    
            self.offers.insert_one(data) #INSERIR FILTRO
            print("Dados inseridos")

    def find(self,query: dict): #busca

        result = self.offers.find_one(query)

        if result is not None:
            print("Dado encontrado")
            return result
            
        else:
            print("Dado nao encontrado")
            
def main():
    
    pass

if __name__ == "__main__":

    main()

    

    


    

import Bot, Crawler, Database
import datetime

class Post:

    def __init__(self): 

        
        self.db = Database.DataBase()
        self.craw = Crawler.Crawler()
        self.bot = Bot.Bot()

    def connect(self): #faz toda a conexao (crawler - banco de dados - postagem)
        
        try:

            datanow = str(datetime.datetime.now().date())
            data = self.craw.extractNecessary()
            self.db.insert(data)
            self.bot.post(self.db.find({'datenow' : datanow}))
            print("postagem concluida")
    
        except Exception as e:

            print("nao foi possivel efetuar a postagem")
            print(e)


def main():

    obj = Post()
    obj.connect()

if __name__ == "__main__":

    main()


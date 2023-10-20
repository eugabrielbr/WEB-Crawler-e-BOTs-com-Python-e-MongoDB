import tweepy 
import os 
from dotenv import load_dotenv
import Crawler,Database
import datetime

class Bot:
    
    def __init__(self): #construtor

        load_dotenv()
        
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET') 

        access_token = os.getenv('ACCESS_TOKEN')
        access_secret = os.getenv('ACCESS_SECRET')

        bearer_token = os.getenv('BEARER_TOKEN')

        self.client = tweepy.Client(
            
            consumer_key = consumer_key,
            consumer_secret = consumer_secret,
            access_token = access_token,
            access_token_secret = access_secret,
            bearer_token = r"{}".format(bearer_token)

        ) 
    
    def titleAlert(self, data: dict): #mensagens de alerta
        
        title = ""
        

        #NAO DEU VELOCIDADE VENTO, FICA PRA PROXIMA ATT
        if ( 30 <= data["mmChuva"] <= 50 and data["porChuva"] != 0):

            title = "🚨 ALERTA AMARELO : RISCO MODERADO 🟡"
            

        elif (100 >= data["mmChuva"] > 50):

            title = "🚨 ALERTA LARANJA : RISCO ALTO 🟠"
           
        
        elif (data["mmChuva"] > 100):

            title = "🚨 ALERTA VERMELHO : GRANDE PERIGO 🔴"
          
        
        elif (data["porChuva"] > 50 ):
            
            title = "🚨 ALERTA : CHANCE DE CHUVA 🌧️"
           

        else:

            if ( 35 > data["tempMax"] > 30):
                
                title = "🚨 ALERTA: QUENTE 🔥" 

            elif ( 40 >= data["tempMax"] >= 35):
                
                title = "🚨 ALERTA: MUITO QUENTE 🔥" 
            

            elif( data["tempMax"] > 40):

                title = "🚨 ALERTA: SUPER QUENTE! ❗🔥" 

            elif (18 >= data["tempMin"] > 15):

                title = "🚨 ALERTA: FRIO! ❄️" 

            elif ( 15 >= data["tempMin"] >= 5):

                title = "🚨 ALERTA: MUITO FRIO! ❄️" 
           
            
            elif (data["tempMin"] < 5):

                title = "🚨 ALERTA: SUPER FRIO! ❗❄️" 
           
            else:

                title = "😎 CLIMA NORMAL" 
      

        return title

        

        
    def post(self, data : dict): #postagem
        
        alertLevel = self.titleAlert(data)

        post = "{}\n\n{}\n\nTemperatura minima: {}° ⬇️\nTemperatura maxima: {}° ⬆️\nPorcentagem de chuva: {} 🌧️\nRaios UV: {} ☀️\n\nMais informações: {} 👇".format(alertLevel,data['title'],data['tempMin'],data['tempMax'], str(data['porChuva']) + "%" + " - " + str(data['mmChuva']) + "mm",data['infos']['Raios UV'],'www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/5764/irara-ba')
        self.client.create_tweet(text = post)
        



def main():

    pass

if __name__ == "__main__":

    main()
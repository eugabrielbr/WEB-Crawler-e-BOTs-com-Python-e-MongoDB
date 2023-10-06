import requests
from bs4 import BeautifulSoup

#1 https://weather.com/weather/today/l/-12.05,-38.77?par=google // nao foi
#2 https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/5764/irara-ba
#3 https://www.cptec.inpe.br/previsao-tempo/ba/irara

class Crawler: 

    def request(self,link: str): #pegando a pag html
        
        response = requests.get(link)
        text = BeautifulSoup(response.text, 'html.parser')
        return text

    def extractFromInpe(self): #filtrando as informacoes encontradas para site INPE

        object = Crawler() 
        
        rawInpe = object.request('https://www.cptec.inpe.br/previsao-tempo/ba/irara')

        temperatureMax = rawInpe.find('span',{'class':'text-danger font-weight-bold'}).text
        temperatureMin = rawInpe.find('span',{'class':'text-primary font-weight-bold'}).text
        title = rawInpe.find('li',{'class':'breadcrumb-item active'}).text
        data = rawInpe.find('h3',{'class':'block-title'}).text

        temperatureMax = int(temperatureMax.replace('°\xa0', ''))
        temperatureMin = int(temperatureMin.replace('°\xa0', ''))
        date = str(data).replace('Previsão numérica de tempo por período ','').replace(')','').replace('(','')
        
        
        data = {
            'tempMax' : temperatureMax,
            'tempMin' : temperatureMin,
            'title' : title,
            'data' : date
        }

        print(data)


def main():


    object = Crawler() 
    object.extractFromInpe()
   


        
main()
        





  

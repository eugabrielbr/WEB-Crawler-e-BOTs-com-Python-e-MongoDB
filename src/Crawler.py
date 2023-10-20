import requests
from bs4 import BeautifulSoup
from datetime import *

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
            'date' : date
        }

        return data
    
    def extractFromClimaTempo(self): #filtrando as informacoes encontradas para site ClimaTempo

        object = Crawler()

        rawClimatempo = object.request('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/5764/irara-ba')
        
        temperatureMaxAndMin = rawClimatempo.find('div',{'class': '-gray _flex _margin-l-5'}).text.replace('\n', '').replace('°','')
        titleInfo = rawClimatempo.find('p',{'class' : '-gray -line-height-24 _center'}).text
        rainPerce = rawClimatempo.find('div',{'class' : '-gray _flex _align-center'}).text.replace('\n', '')
        date = rawClimatempo.find('div',{'class' : 'date-inside-circle'}).text.replace('\n','').replace('sex','/sex')
        
        general = rawClimatempo.find_all('div',{'class': 'description'})
      
        dicAlert = {}
        listaTempTitle = [] 
        listaTempValue = []
      
        for y in general: 

            try:
                title = y.find('p',{'class': 'title'}).text #extraindo todas as informacoes com essas referencias
                value = y.find('p',{'class': 'value'}).text  
                listaTempTitle.append(title)
                listaTempValue.append(value)
            except:
                continue
                
        for i,j in zip(listaTempTitle,listaTempValue):
            
            newTitle = str(i.replace('\n',''))
            newValue = str(j.replace('\n',''))

            dicAlert[newTitle] = newValue 
            
        
        tempMin = int(temperatureMaxAndMin[0] + temperatureMaxAndMin[1])
        tempMax = int(temperatureMaxAndMin[2] + temperatureMaxAndMin[3])
        
        data = {
            
            'title' : titleInfo,
            'tempMax': tempMax,
            'tempMin' : tempMin,
            'Infos' : dicAlert,
            'porChuva' : rainPerce,
            'date': date
         
        }

        return data
    
    def extractNecessary(self):

        data = self.extractFromInpe()
        data2 = self.extractFromClimaTempo()
        dateNow = str(datetime.now().date())
        
        posMmChuva = data2['porChuva'].rfind("m")
        mmChuva = str(data2['porChuva'])[:posMmChuva].replace("m","");

        posPorChuva = data2['porChuva'].rfind("-")
        porChuva = str(data2['porChuva'])[posPorChuva:].replace("-","").replace("%","").replace(" ", "");

        mmChuva = int(mmChuva)
        porChuva = int(porChuva)

        newData = {
            
            'title' : data2['title'],
            'tempMax' : data['tempMax'],
            'tempMin' : data['tempMin'],
            'dateData1' : data['date'],
            'dateData2' : data2['date'],
            'porChuva' : porChuva,
            'mmChuva' : mmChuva,
            'infos' : data2['Infos'],
            'datenow' : dateNow
            
        }
        
        return newData      

def main():

   pass
    
#mto tbr fzr excecoes personalizadas, um dia implementarei mas este dia nao é hj
if __name__ == "__main__":
    main()
        





  

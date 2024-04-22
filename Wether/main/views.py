from django.shortcuts import render
from .models import WeatherData
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 

def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here " '''
        
        # source contain JSON data from API 
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&appid=c64591f66f7a88786a864d25be04c904').read() 

        # converting JSON data to a dictionary 
        
        list_of_data = json.loads(source) 
        temperature_kelvin = list_of_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        
        wdata = WeatherData()
        
        # data for variable list_of_data 
        data = {
            'city':city,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(round(temperature_celsius, 2)) + '°C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        
        wdata.city = city
        wdata.country_code = str(list_of_data['sys']['country'])
        wdata.coord = str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat'])
        wdata.temp = str(round(temperature_celsius, 2)) + '°C'
        wdata.pressure = str(list_of_data['main']['pressure'])
        wdata.humidity = str(list_of_data['main']['humidity'])
        wdata.save()

        bdata = WeatherData.objects.all().order_by('-timestamp')
        
        


        print(data) 
    else: 
        data ={}
    return render(request, "main/index.html", data) 

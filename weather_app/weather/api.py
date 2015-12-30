import json
import requests
import urllib, urllib2
API_KEY = '7680abfcdf81d1cdb66896eceaf8ba45'
#url = 'http://api.openweathermap.org/data/2.5/weather?q=paris&appid=7680abfcdf81d1cdb66896eceaf8ba45'
#{"temp":280.81,"pressure":1016,"humidity":93,"temp_min":280.15,"temp_max":281.15}
def run_query(search_term):
    root_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    search_url = root_url+search_term+'&appid='+API_KEY
    json_obj = urllib2.urlopen(search_url)
    data = json.load(json_obj)
    item =  data['main'] 
    result = []
    result.append('city name = '+str(search_term))

    for da in item.keys():
         result.append(str(da)+'='+str(item[da]))
    
    #dic = {'temperature':item['temp'],'pressure':item['pressure'],'humidity':item['humidity'],'city name':str(search_term)}
    item = data['wind']
    result.append('wind speed ='+str(item['speed']))
    result.append('angle ='+str(item['deg']))
    #result.append(dic)
    return result
    #for item in data['main']:
    # item['temp'],item['pressure'],item['humidity'],item['temp_min'],item['temp_max']
         
print run_query('delhi')

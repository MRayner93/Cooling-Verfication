"""
THIS FILE IS TO TEST WEATHER DATA ONLY. THIS FUNCTION WILL BE IMPLEMENTED IN THE FUNCTIONS.PY LATER!
"""
import requests
import json
from datetime import datetime

 
def check_weather(weatherdata_list, time_out):
    
    weatherdata = weatherdata_list[0]
# Example
    api_key = "F5PA3TTVTMFF3D83AQJBAH3A3"
    location = weatherdata[1],"DE"
    datetime_str = time_out.strftime('%Y-%m-%dT%H:%M:%S')
    hour = time_out.hour
# Convert time to string
    
# Visual Crossing Weather 
    url ='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{timestamp}'.format(location=location, timestamp=datetime_str)
    response = requests.get(url, params={'unitGroup': 'metric','key':
    api_key,'include': 'hours'})
    data = response.json()

    temperature = data["datetime"][hour]["temp"]
    
    return(temperature)

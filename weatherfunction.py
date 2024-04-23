"""
THIS FILE IS TO TEST WEATHER DATA ONLY. THIS FUNCTION WILL BE IMPLEMENTED IN THE FUNCTIONS.PY LATER!
"""
import requests
import json
from datetime import datetime

 
def check_weather(encrypted_transportstation_data , timestamp):
    post_code = encrypted_transportstation_data[3]
# Example
    api_key = "F5PA3TTVTMFF3D83AQJBAH3A3"
    location = post_code,"DE"
    datetime = timestamp

# Convert time to string
    
# Visual Crossing Weather 
    url ='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{timestamp}'.format(location=location, timestamp=datetime)
    response = requests.get(url, params={'unitGroup': 'metric','key':
    api_key,'include': 'hours'})
    data = response.json()
    temperature = data["days"][0]["temp"]
    
    return(temperature)

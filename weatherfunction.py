"""
THIS FILE IS TO TEST WEATHER DATA ONLY. THIS FUNCTION WILL BE IMPLEMENTED IN THE FUNCTIONS.PY LATER!
"""
import requests
import json
from datetime import datetime

 
def check_weather(decrypted_company_data):
    post_code = decrypted_company_data[4]
# Example
    api_key = "F5PA3TTVTMFF3D83AQJBAH3A3"
    location = post_code,"DE"
    datetime_str = "12.07.2023 15:00"

# Convert time to string
    datetime_obj = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
    timestamp = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S')

# Visual Crossing Weather 
    url ='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{timestamp}'.format(location=location, timestamp=timestamp)
    response = requests.get(url, params={'unitGroup': 'metric','key':
    api_key,'include': 'hours'})
    data = response.json()
    temperature = data["days"][0]["temp"]
    
    return(temperature)

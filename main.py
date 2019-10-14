#print: 
#- current weather outside
#- what the weather in manhattan will be for the day
#- high/low
#- precipitation
#- temp for next 7 hours

import requests, json

#weather_api key= 'cdb525110e5845c9a400e26c152e0ce4'

def current_weather():
    weather_api_url = "https://api.weatherbit.io/v2.0/current?postal_code=11213&country=united%20states&key=cdb525110e5845c9a400e26c152e0ce4"
    
    parameters = {"lon": -73.9467, "lat":40.67}
    response = requests.get(weather_api_url, params=parameters)
    """
    status_code = response.status_code

    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}")
    else:
    """
    response_json = response.json()
    records = response_json
    print(records)    
    
    #return response_json["city_name"]

if __name__ == "__main__":
    
    current_weather()
"""
    for result in results:
        city = result["city_name"]
        time = result["datetime"]
        precip = result["precip"]
        temp = result["temp"]
"""
#Step 1
#Write a python script that consumes a public weather api and print information. Include the following ...
#link to api: https://www.weatherbit.io/api
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

    response_json = response.json()
    records = response_json
    temp = records['data'][0]['temp']
    chance_of_rain = records['data'][0]['precip']
    print(f"The weather outside is: {temp}")
    print(f"The chance of rain is: {chance_of_rain}")
    """
    with open('records.json', 'w') as fp:
        json.dump(records, fp)
    """

if __name__ == "__main__":
    current_weather()
from sys import api_version
import requests 

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "8073c810ed340d52995048411f73382b"

weather_params = {
    "lat": 44.424110,
    "lon": 18.036591,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}


response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True 


if will_rain:
    print("Bring an umbrella.")

else:
    print("You don't need an umbrella today!")

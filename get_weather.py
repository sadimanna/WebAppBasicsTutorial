import requests



def get_weather(city, W_API_KEY):
    url = f"http://api.weatherapi.com/v1/current.json?key={W_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "City not found"}

if __name__ == "__main__":
    W_API_KEY = "ae72f9378f3d4c37b98113340252509"
    city = input("Enter city name: ")
    weather_info = get_weather(city, W_API_KEY)
    # print(weather_info)
    print("Location: ", weather_info.get('location').get('name'))
    print("Latitude: ", weather_info.get('location').get('lat'), end=' ')
    print("Longitude: ", weather_info.get('location').get('lon'))
    # print(weather_info.get('current'))
    print("Current Temperature (C): ", weather_info.get('current').get('temp_c'))
    print("Current Condition: ", weather_info.get('current').get('condition').get('text'))
    print("Wind (KPH): ", weather_info.get('current').get('wind_kph'))
    print("Precipitation (mm):",weather_info.get('current').get('precip_mm'))
    print("Humidity: ",weather_info.get('current').get('humidity'))
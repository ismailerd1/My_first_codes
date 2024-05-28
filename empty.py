import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Birimleri Celsius olarak ayarla
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        city = weather_data['name']

        print(f'Hava Durumu Bilgileri - {city}:')
        print(f'Sıcaklık: {temperature}°C')
        print(f'Durum: {description}')
    else:
        print('Hava durumu bilgileri alınamadı.')

def main():
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    city = input('Lütfen hava durumu bilgisini öğrenmek istediğiniz şehri girin: ')

    weather_data = get_weather(api_key, city)

    display_weather(weather_data)

if __name__ == "__main__":
    main()

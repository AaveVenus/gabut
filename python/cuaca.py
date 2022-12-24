import requests
import datetime

today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)

print("Hari ini adalah:", today.strftime("%A, %d %B %Y"))
print("Besok adalah:", tomorrow.strftime("%A, %d %B %Y"))

api_key = "c8ab84cd6b8a68d49f57209487e8fd5c"
city_id = "1636722"
url = f"http://api.openweathermap.org/data/2.5/weather?id=1636722&appid=c8ab84cd6b8a68d49f57209487e8fd5c"

response = requests.get(url)
data = response.json()

print("Cuaca saat ini di kota Anda adalah:", data['weather'][0]['description'])
print("Suhu saat ini adalah:", data['main']['temp'], "derajat Celcius")
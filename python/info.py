import datetime
import requests

kota = input('Masukkan nama kota: ')
negara = "Indonesia"

def hari_ini():
  sekarang = datetime.datetime.now()
  nama_hari = sekarang.strftime('%A')
  
  return nama_hari

def waktu_sekarang():
  sekarang = datetime.datetime.now()
  jam = sekarang.strftime('%H')
  menit = sekarang.strftime('%M')
  
  return f'{jam}:{menit}'

def ambil_cuaca(kota):
  api_key = 'c8ab84cd6b8a68d49f57209487e8fd5c'
  url = f'https://api.openweathermap.org/data/2.5/weather?q={kota}&units=metric&appid={api_key}'
  data = requests.get(url).json()
  
  cuaca = data['weather'][0]['main']
  suhu = data['main']['temp']
  
  return f'Cuaca saat ini di {kota} adalah {cuaca} dengan suhu {suhu:.1f}°C'

url = f'https://api.aladhan.com/v1/timingsByCity?city={kota}&country={negara}&method=2'
response = requests.get(url)
data = response.json()

print()
print(f'Hari ini adalah {hari_ini()}')
print(f'Waktu sekarang adalah {waktu_sekarang()}')
print(ambil_cuaca(kota))
print(f"Jadwal sholat hari ini di {kota}, {negara}:")
print(f"Shubuh  : {data['data']['timings']['Fajr']}")
print(f"Dzuhur  : {data['data']['timings']['Dhuhr']}")
print(f"Ashar   : {data['data']['timings']['Asr']}")
print(f"Maghrib : {data['data']['timings']['Maghrib']}")
print(f"Isya    : {data['data']['timings']['Isha']}")
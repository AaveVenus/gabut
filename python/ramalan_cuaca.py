import requests

def ambil_ramalan_cuaca(kota):
  # mengambil data ramalan cuaca dari API OpenWeatherMap
  api_key = 'c8ab84cd6b8a68d49f57209487e8fd5c'
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}'
  data = requests.get(url).json()
  
  # mengekstrak informasi ramalan cuaca dari data yang didapat
  ramalan_cuaca = []
  for item in data['list']:
    tanggal = item['dt_txt']
    cuaca = item['weather'][0]['main']
    suhu = item['main']['temp'] - 273.15  # konversi dari Kelvin ke Celcius
    ramalan_cuaca.append({'tanggal': tanggal, 'cuaca': cuaca, 'suhu': suhu})
  
  # mengembalikan informasi ramalan cuaca
  return ramalan_cuaca

# meminta input nama kota dari user
kota = input('Masukkan nama kota: ')

# menampilkan informasi ramalan cuaca
ramalan_cuaca = ambil_ramalan_cuaca(kota)
print(f'Ramalan cuaca di {kota}:')
for item in ramalan_cuaca:
  print(f' - Tanggal: {item["tanggal"]}, Cuaca: {item["cuaca"]}, Suhu: {item["suhu"]:.2f} derajat Celcius')

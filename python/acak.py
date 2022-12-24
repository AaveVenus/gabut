import random
import time

menu_makanan = [
    'bakso',
    'thelap thelep',
    'beli di pak dji',
    'mie ayam',
    'masak sendiri wkwkw',
    'nasi goreng',
    'lalapan',
    'di ayam ngamok',
    'roti aok aok aok',
    'mie pangsit',
    'mueslie'
]

menu_minuman = [
    'jus pisang',
    'air degan',
    'jus jeruk',
    'air mineral',
    'jamu',
    'susu',
    'jahe'
]

menu_healing = [
    
]

print(f'Jeng jeng jeng makanan hari ini adalah')
time.sleep(2)
makanan = random.choice(menu_makanan)
minuman = random.choice(menu_minuman)
print(f'Jadi kita makan {makanan}')
print(f'Minumannya adalah {minuman}')
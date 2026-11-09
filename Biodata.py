nama = input("Siapa nama kamu? : ")
kota_asal = input("Dari kota mana kamu berasal? : ")
tahun_lahir = int(input("Tahun berapa kamu lahir? : "))
hobi = input("Apa hobi kamu ? : ")
umur = 2026 - tahun_lahir
umur_bulan = umur*12


print("\n" + "="*30)
print("       KARTU PERKENALAN       ")
print("="*30)
print(f"Nama                : {nama}")
print(f"Kota Asal           : {kota_asal}")
print(f"Tahun Lahir         : {tahun_lahir}")
print(f"Hobi                : {hobi}")
print(f"Umur                : {umur} tahun")
print(f"Umur dalam Bulan    : {umur_bulan} bulan")
print("="*30)
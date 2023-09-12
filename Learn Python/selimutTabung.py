#program untuk menghitung volume dan luas selimut tabung

#import packages math

import math



diameter = float(input("Diameter lingkaran (d)= "))

tinggi = float(input("Tinggi tabung (t)= "))



luas_lingkaran = 0.25*math.pi*diameter**2

keliling_lingkaran = math.pi*diameter

luas_persegi_panjang = tinggi*keliling_lingkaran

volume_tabung = round(luas_lingkaran*tinggi,2)

luas_selimut_tabung = round((2*luas_lingkaran) + luas_persegi_panjang,2)



print(f"\nVolume tabung= {volume_tabung} satuan volume")

print(f"Luas selimut tabung= {luas_selimut_tabung} satuan luas")
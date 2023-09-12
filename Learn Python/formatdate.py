#program untuk mengubah teks menjadi format tanggal

#import packages datetime

from datetime import datetime



hari = str(input("Masukkan tanggal: "))

bulan = str(input("Masukkan bulan (angka): "))

tahun = str(input("Masukkan tahun (lengkap): "))

jam = str(input("Masukkan jam: "))

menit = str(input("Masukkan menit: "))



tanggal = hari + ' ' + bulan + ' ' + tahun + ' ' + jam + ':' + menit



datetime_object = datetime.strptime(tanggal, "%d %m %Y %H:%M")



print(type(datetime_object))

print(datetime_object)

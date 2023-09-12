#program untuk cek angka ganjil atau genap secara acak

n1 = int(input("Masukkan angka pertama: "))

n2 = int(input("Masukkan angka kedua: "))



for i in range(n1,n2+1):

  if i % 2 == 0:

    res = 'Genap'

  elif i % 2 != 0:

    res = 'Ganjil'

  print(i,res)

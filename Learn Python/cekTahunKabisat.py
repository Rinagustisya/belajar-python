#program untuk cek tahun kabisat

number_of_year = int(input("Berapa banyak tahun yang ingin kamu ketahui? "))

year_input = []

for _ in range(0,number_of_year):

  year_input.append(int(input("Masukkan tahun= ")))



#jika tahun dapat dibagi 100 maka termasuk century year

#century year dapat dibagi 400 maka tahun tersebut adalah tahun kabisat

for i in year_input:

  if (i % 100 == 0) and (i % 400 == 0):

    res = 'Kabisat'



#jika tahun tidak dapat dibagi 400 maka bukan century year

#bukan century year jika dapat dibagi 4 maka tahun tersebut adalah tahun kabisat

  elif (i % 100 != 0) and (i % 4 == 0):

    res = 'Kabisat'



#jika kedua syarat diatas tidak memenuhi maka tahun tersebut bukan tahun kabisat

  else:

    res = 'Bukan Kabisat'



  print(i,res)
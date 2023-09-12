#program untuk menghitung luas segitiga

a = float(input("Jarak a= "))

b = float(input("Jarak b= "))

c = float(input("Jarak c= "))



#menghitung semi-paramater

s = (a+b+c)/2



#menghitung luas segitiga

area = (s*(s-a)*(s-b)*(s-c))**0.5



print(f"Luas area segitiga adalah {round(area,2)} satuan unit luas")
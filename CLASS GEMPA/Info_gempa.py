from Gempa import *

#Membuat Objek Gempa dengan Lokasi dan Skala
gempa1 = gempa("Banten",1.2)
gempa2 = gempa("Palu",6.1)
gempa3 = gempa("Cianjur",5.6)
gempa4 = gempa("Jaya Pura",3.3)
gempa5 = gempa("Garut",4.0)


#Info Gempa
print("## Gempa Bumi Info ##")
print()
gempa1.dampak() #Memanggil Method dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()
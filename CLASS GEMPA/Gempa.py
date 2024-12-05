class gempa:
    #konstruktur inisialisasi atribut
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala

    # method penentu skala gempa
    def dampak(self):
        #logika/statement
        if self.skala < 2:
            print("gempa tidak berasa")
        elif self.skala >= 2  and self.skala <= 4 :
                print("gempa berdampak bangunan retak")
        elif self.skala >= 4  and self.skala <= 6 :
                print("gempa berdampak bangunan retak")
        elif self.skala > 6:
                print("gempa besar berdampak tsunami")

            #Menampilkan Lokasi Dan Skala Gempa
        print(f"lokasi Gempa:{self.lokasi}")
        print(f"Skala Gempa:{self.lokasi}")
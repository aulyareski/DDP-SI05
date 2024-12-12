from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup,berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.jenis = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah warna {self.warna} dan hewan ini jenisnya ular {self.jenis}')

kobra = ular('kobra', 'tikus', 'amphibi', 'bertelur', 'hitam', 'beracun')
kobra.cetak_ular()

sanca = ular('sanca', 'tikus', 'amphibi', 'bertelur', 'orange', 'beracun')
sanca.cetak_ular()

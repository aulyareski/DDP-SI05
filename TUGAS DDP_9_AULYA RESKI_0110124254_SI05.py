def celcius_ke_fahrenhei(cecius):
    print(cecius * 9/5 + 32)
celcius_ke_fahrenhei(0)


print('=== MENCARI BILANGAN GENAB ===')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('=== keterangan lulus dan tidak lulus ===')
#rata" nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print('lulus')
    else:
        print('gagal')
skor(80)
skor(80)


print('\n---- mencetak bilangan ganjil ----')
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=' ')
    bil_ganjil(20)
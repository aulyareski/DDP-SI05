#tugas no1
kendaraan = [
    "Honda", "Beat", "140cc", "hitam", 2
]
kendaraan.append("Rp.17.000.000")
kendaraan.append("B234")
kendaraan[1] = "Honda "
print(kendaraan)


# tugas 2
pilih = int(input('Selamat datang di aplikasi menghitung\n'
                  '1. Untuk menghitung luas persegi\n'
                  '2. Untuk menghitung luas lingkaran\n'
                  '3. Untuk menghitung luas segitiga\n'
                  'Masukkan pilihan: '))

match pilih:
    case 1:
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukkan sisi persegi: "))
        luaspsg = sisi * sisi
        print("Luas persegi yang sisinya", sisi, "adalah", luaspsg)

    case 2:
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = int(input("Masukkan jari-jari lingkaran: "))
        luaslkr = 3.14 * jari2 * jari2
        print("Luas lingkaran yang jari-jarinya", jari2, "adalah", luaslkr)

    case 3:
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        luasseg = 0.5 * alas * tinggi
        print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luasseg)

    case _:
        print("Pilihan tidak valid")
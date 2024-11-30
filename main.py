import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling =sisi*sisi*sisi*sisi
    print(f'luas persegi {sisi} * {sisi} = {luas}')
    print(f"keliling persegi adalah {keliling}")
    
def persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    print(f"hasil luas persegi panjang dari, {panjang} * {lebar} = {luas}")

def l_segitiga(alas,tinggi):
        luas = 0,5 * alas * tinggi
        print(f"hasil luas segitiga adalah {alas} * {tinggi} = {luas} ")

def l_lingkaran(j1,j2,):
    luas = 22/7 * j1 * j2
    print(f"hasil luas segitiga adalah {j1} * {j2} ")
    
def l_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    print(f"hasil luas jajargenjang adalah {alas} * {tinggi} = {luas}")

    #bamgun ruang

    import math

# Volume and Surface Area of Cube
def volume_kubus(sisi):
    volume = sisi ** 3  # Volume of a cube is sisi^3
    luas_permukaan = 6 * (sisi ** 2)  # Surface area of a cube is 6 * sisi^2
    print(f'Volume kubus dengan sisi {sisi} adalah {volume}')
    print(f'Luas permukaan kubus dengan sisi {sisi} adalah {luas_permukaan}')

# Volume and Surface Area of Rectangular Prism (Balok)
def volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi  # Volume of rectangular prism
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)  # Surface area
    print(f'Volume balok dengan panjang {panjang}, lebar {lebar}, dan tinggi {tinggi} adalah {volume}')
    print(f'Luas permukaan balok adalah {luas_permukaan}')

# Volume and Surface Area of Cone
def volume_tirus(jari_jari, tinggi):
    volume = (1/3) * math.pi * jari_jari ** 2 * tinggi  # Volume of a cone
    luas_permukaan = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari ** 2 + tinggi ** 2))  # Surface area
    print(f'Volume tirus dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah {volume}')
    print(f'Luas permukaan tirus adalah {luas_permukaan}')

# Volume and Surface Area of Sphere
def volume_bola(jari_jari):
    volume = (4/3) * math.pi * jari_jari ** 3  # Volume of a sphere
    luas_permukaan = 4 * math.pi * jari_jari ** 2  # Surface area of a sphere
    print(f'Volume bola dengan jari-jari {jari_jari} adalah {volume}')
    print(f'Luas permukaan bola adalah {luas_permukaan}')

# Volume and Surface Area of Cylinder
def volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari ** 2 * tinggi  # Volume of a cylinder
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)  # Surface area of a cylinder
    print(f'Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah {volume}')
    print(f'Luas permukaan tabung adalah {luas_permukaan}')

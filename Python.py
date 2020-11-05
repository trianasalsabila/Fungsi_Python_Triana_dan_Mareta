# Fungsi_Python_Triana_dan_Mareta
#Program Menghitung Luas dan Keliling Bangun Datar
#Jobsheet 4 Dasar Pemrograman

#SISTEM PEMBELAJARAN MATEMATIKA

def luas_bujur_sangkar(s):
    luas = s*s
    return luas
def keliling_bujur_sangkar(s):
    keliling = 4*s
    return keliling
def luas_persegi_panjang(p,l):
    luas = p*l
    return luas
def keliling_persegi_panjang(p,l):
    keliling = 2*(p+l)
    return keliling
def luas_segitiga(a,t):
    luas = 0,5*a*t
    return luas
def keliling_segitiga(a,t):
    keliling = a+b+c
    return keliling
def luas_lingkaran(r):
    luas = 3,14*r*r
    return luas
def keliling_lingkaran(r):
    keliling = 2*3,14*r
    return keliling
def luas_jajar_genjang(a,t):
    luas = a*t
    return luas
def keliling_jajar_genjang(a,t):
    keliling = 2*(a+b)
    return keliling
    
pilihan-1
while pilihan!-0:
    print("1- Menghitung Luas bujur sangkar")
    print("2- Menghitung Keliling bujur sangkar")
    print("3- Menghitung Luas persegi panjang")
    print("4- Menghitung Keliling persegi panjang")
    print("5- Menghitung Luas segitiga")
    print("6- Menghitung Keliling segitiga")
    print("7- Menghitung Luas lingkaran")
    print("8- Menghitung Keliling lingkaran")
    print("9- Menghitung Luas jajar genjang")
    print("10- Menghitung Keliling jajar genjang")

    pilihan=int(input("Masukkan Pilihan Anda"))
    print('')
    print('')
    if pilihan==1 :
        print("Luas bujur sangkar")
        print('')
        s=int(input("Masukkan sisi :"))
        print("Luas bujur sangkar adalah :", luas_bujur_sangkar(s))
        print('')
        print('')
    elif pilihan==2 :
        print("Keliling bujur sangkar")
        print('')
        s=int(input("Masukkan sisi :")
        print("Keliling bujur sangkar adalah :", keliling_bujur_sangkar(s))
        print('')
        print('')
    if pilihan==3 :
        print("Luas persegi panjang")
        print('')
        p=int(input("Masukkan panjang :"))
        l=int(input("Masukkan lebar :"))
        print("Luas persegi panjang adalah :", luas_persegi_panjang(p,l))
        print('')
        print('')
    elif pilihan==4 :
        print("Keliling persegi panjang")
        print('')
        p=int(input("Masukkan panjang :"))
        l=int(input("Masukkan lebar :"))
        print("Keliling persegi panjang adalah :", keliling_persegi_panjang(p,l))
        print('')
        print('')
    if pilihan==5 :
        print("Luas segitiga")
        print('')
        a=int(input("Masukkan alas :"))
        t=int(input("Masukkan tinggi :"))
        print("Luas segitiga adalah :", luas_segitiga(a,t))
        print('')
        print('')
    elif pilihan==6 :
        print("Keliling segitiga")
        print('')
        a=int(input("Masukkan alas :"))
        t=int(input("Masukkan tinggi :"))
        print("Keliling segitiga adalah :", keliling_segitiga(a,t))
        print('')
        print('')
    if pilihan==7 :
        print("Luas lingkaran")
        print('')
        s=int(input("Masukkan jari jari :"))
        print("Luas lingkaran adalah :", luas_lingkaran(r))
        print('')
        print('')
    elif pilihan==8 :
        print("Keliling lingkaran")
        print('')
        s=int(input("Masukkan jari jari :")
        print("Keliling lingkaran adalah :", keliling_lingkaran(r))
        print('')
        print('')
    if pilihan==9 :
        print("Luas jajar genjang")
        print('')
        a=int(input("Masukkan alas :"))
        t=int(input("Masukkan tinggi :"))
        print("Luas jajar genjang adalah :", luas_jajar_genjang(a,t))
        print('')
        print('')
    elif pilihan==10 :
        print("Keliling jajar genjang")
        print('')
        a=int(input("Masukkan sisi a :"))
        b=int(input("Masukkan sisi b :"))
        print("Keliling jajar genjang adalah :", keliling_jajar_genjang(a,b))
        print('')
        print('')
    else:
        print("Input yang Anda masukkan salah")
        print('')
        print('')

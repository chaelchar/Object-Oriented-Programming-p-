'''Latihan fungsi'''
import os
# program menghitung luas dan keliling persegi panjang
# membuat header program
def header():
    os.system('cls')
    print(f"{'PROGRAM HITUNG LUAS-KELILING':^40}")
    print(f"{'PERSEGI PANJANG':^40}")
    print(f"{40*'-':^40}")

# mengambil user input
def input_nilai():
    lebar   = int(input("input Lebar   -> ")) 
    panjang = int(input("input PANJANG -> ")) 
    return lebar,panjang

# program menghitung luas

def hitung_luas (lbr,pnjg):
    luas = pnjg * lbr
    return luas

def hitung_keliling(lbr,pnjng):
    keliling = 2*(lbr + pnjng)
    return keliling

# tampilkan hasilnya
def hasil(LUAS:0,KELILING:0):
    if KELILING == 0:
        print(f"Hasil hitung Luas     -> {LUAS}")
    elif LUAS   == 0:    
        print(f"Hasil hitung keliling -> {KELILING}")
    else:
        print(f"Hasil hitung Luas     -> {LUAS}")
        print(f"Hasil hitung keliling -> {KELILING}")


def luas_keliling():
    pilih = int(input("menghitung 1.luas/2.keliling/3.dua-duanya --> "))
    if (pilih-1) == 0:
        return 0
    elif (pilih-1) == 1:
         return 1
    else:
        return 2

while True:
    header()
    LEBAR,PANJANG = input_nilai()
    CHOICE = luas_keliling()  

    if  CHOICE == 0:
        LUAS = hitung_luas(LEBAR,PANJANG)
        hasil(LUAS,KELILING=0)
    elif CHOICE == 1:
        KELILING = hitung_keliling(LEBAR,PANJANG) 
        hasil(LUAS=0,KELILING=KELILING)
    else:
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        hasil(LUAS,KELILING)

    continu = input("hitung lagi ??(y/n) -> ")
    if continu != 'y':
        break
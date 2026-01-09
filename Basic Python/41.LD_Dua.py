import datetime
import os
import random
import string

# template dict mahasiswa
mahasiswa_template = {
    'nama': '',
    'nim': '',
    'sks': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
# dictionary kosong 
data_mahasiswa = {}

while True:
    os.system("cls")
#makan yg itu  
#makan yg itu  
    print("")
    print(f"{'SELAMAT DATANG':^40}")
    print(f"{'DATA MAHASISWA':^40}")
    print("-"*50)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    print(mahasiswa)

    mahasiswa['nama'] = input("Masukkan nama: ")
    mahasiswa['nim']  = input("Masukkan NIM: ")
    mahasiswa['sks']  = int(input("Masukkan SKS: "))
    TAHUN_LAHIR       = int(input("Input Tahun (YYYY) -> "))
    BULAN_LAHIR       = int(input("Input Bulan (MM) -> "))
    TANGGAL_LAHIR     = int(input("Input Tanggal (DD) -> "))
    mahasiswa['lahir']= datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for _ in range(8)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"{'KEY':<6}  {'NAMA':<10}  {'NIM':<10}  {'SKS':<5} {'LAHIR':<12}")
    print("-"*60)
    for KEY in data_mahasiswa:
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir']
        print(f"{KEY:<6} {NAMA:<10} {NIM:<10} {SKS:<5} {LAHIR}")

    print("\n")
    continu = input("lanjut atau tidak (y/n)? ->")
    if continu == 'n':
        break
    else:
        continue

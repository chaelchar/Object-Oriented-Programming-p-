import datetime
import os

# template dict mahasiswa
mahasiswa_template = {
    'nama': '',
    'nim': '',
    'sks': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
# dictionary kosong 
os.system("cls")
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
print(mahasiswa)
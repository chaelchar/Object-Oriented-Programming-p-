'''Default Argument'''

# defaultf argument: nilai alternatifnya
# kalo semisal parameter 1 ngk di-isi
# bisa lanjut ke parameter berikutnya

# contoh 1
def apakabar(sapa = "hallo"):
    '''Fungsi dengan Default Argument'''
    print(f"{sapa} Michael")

apakabar("Apakabar")
apakabar()

# contoh 2
def sapa(pesan,nama = 'michael'):
    print(f"{pesan} {nama}")

sapa('selamat siang')

# contoh 3
def pangkat(angka,pangkat):
    return angka**pangkat

print(f"hasil pangkat -> {pangkat(2,3)}")
hasil = pangkat(angka=5,pangkat=2)
print(f"hasil pangkat -> {hasil}")

# contoh 4
def fungsi(input_1 = 1,input_2 = 2,input_3 = 3,input_4 = 4):
    return input_1 + input_2 + input_3 + input_4

print(f"hasil -> {fungsi()}")
print(f"hasil -> {fungsi(input_3=10)}")
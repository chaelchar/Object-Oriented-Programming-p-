'''Fungsi Dengan Argument'''

def hello_world(nama):
    '''Menerima inputan dengan variabel nama'''
    print(f"Selamat datang {nama}")

hello_world("Lambok")

# program tambah

def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"Hasilnya {angka_1} + {angka_2} -> {hasil}")

tambah(1,5)
tambah(23,32)

def fungsi(data):
    '''fungsi peserta'''
    for peserta in data:
        print(f"peserta -> {peserta}")


peserta = ['kael','lambok','ferdi']
fungsi(peserta)

# itukan didalam fungsi
# klo semisal kita ubah data didalam fungsi, ada kemungkinan
# data diluarnya akan ikut terubah juga

print("")

def fungsi_2(data):
    '''fungsi coppy'''
    data_peserta = data.copy()
    for peserta in data_peserta:
        print(f"peserta -> {peserta}")

peserta_2 = ['kael','lambok','ferdi']
fungsi(peserta_2)

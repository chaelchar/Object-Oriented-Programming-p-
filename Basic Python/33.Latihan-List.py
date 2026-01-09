# Program List Buku
# bikin dulu teks = "Masukan data buku".center(25, "-")
teks = "Masukan data buku".center(25, "-")

list_buku = []
while True:
    print(teks)
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print("Buku berhasil ditambahkan!")
    lagi = input("Tambah buku lagi? (ya/tidak): ")
    if lagi.lower() != "y":
        break

print("\nDaftar Buku:")
for i, b in enumerate(list_buku, start=1):
    print(f"{i}| Judul: {b[0]}\n | Penulis: {b[1]}\n")

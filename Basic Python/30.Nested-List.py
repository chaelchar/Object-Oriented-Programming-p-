data_0 = [1,2]
data_1 = [4,1]
data_2 = [4,3,2]

data_list = [1,2,3,4,5]
print(data_list)

list_2D = [data_0,data_1]
print(list_2D)

# contoh penggunaan

mahasiswa_0 = ["Michael", 18, "Laki-Laki"]
mahasiswa_1 = ["gamaliel", 15, "Perempuan"]
mahasiswa_2 = ["lambok", 16, "Laki-Laki"]

list_mahasiswa = [mahasiswa_0,mahasiswa_1,mahasiswa_2]
# cara eksekusinya ada 2
# 1
print("Eksekusi Pertama")
print(list_mahasiswa)

# 2
print("Eksekusi Kedua")
for i in list_mahasiswa:
    print("Data : ",i)

# dan bisa disempurnakan menjadi
print("\n")
teks = "DATA MAHASISWA"
print(f"{teks.center(30,"-")}")
for mahasiswa in list_mahasiswa:
    print(f"Nama      --> {mahasiswa[0]}")
    print(f"umur      --> {mahasiswa[1]}")
    print(f"J.Kelamin --> {mahasiswa[2]}\n")

# dengan reference

list_copy = list_mahasiswa.copy();
print("Mahasiswa -->{}".format(list_copy))
mahasiswa_0[0] = "Eshar"

print("-----LIST COPY-----")
for mahasiswa in list_copy:
    print(f"Nama :{mahasiswa[0]}\n")

print("-----LIST ASLI-----")
for mahasiswa in list_mahasiswa:
    print("Nama: {}\n".format(mahasiswa[0]))

# walaupun sudah di coppy, yang dicopy hanya si list_mahasiswa
# tetapi elemen dalam list_mahasiswa itu tidak dicopy
# jadi list didalam list, hanya mengcopy list luar aja, tidak didalamnya
# jadinya isinya tetap dapat berubah
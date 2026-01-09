# Operasi Dictionary

data_dict = {
    "key1": "mikael",
    "key2": "lambo",
    "key3": "gama"
}

# panjang dictionary
print("")
print("-----Panjang Dictionary-----")
LEN_DICT = len(data_dict)
print("Panjang dictionary:", LEN_DICT)  

# mengecek key existing
print("Apakah 'key1' ada di data_dict? ->", 'key1' in data_dict)
print("Apakah 'key4' ada di data_dict? ->", 'key4' in data_dict)

print("")
print("-----Cek Key-----")

KEY = "key2"
CHECK = KEY in data_dict
print(f"Apakah [{KEY}] ada di data_dict? ->{CHECK}")

# bisakah ubah semua judul yang saya buat
# menjadi ----judulnya-----

# mengakses value(read) tanpa get
print("")
print("-----Mengakses Data-----")
print(f"Data -> {data_dict['key2']}")
# mengakses value(read) dengan get
print(f"Data -> {data_dict.get('key2')}")
# kalau semisal ngk ada
print(f"Data -> {data_dict.get('key4')}")
# hasilnya --> none || tapi bisa kita atur teksnya
print(f"Data -> {data_dict.get('key5','ngk ada disini')}")

# meng-update data
print("")
print("-----Meng-update Data-----")

data_dict['key2'] = 'lambo_updated'
print(f"Data -> {data_dict.get('key2')}") 

# meng-update data dengan .update()
# 1.kalo data sudah ada --> akan meng-overwrite(mengubah)
# 2.kalo data blm   ada --> akan meng-insert(menambah) otomatis

data_dict.update({"key1": "mikael_updated"})
data_dict.update({"key4": "Ferdi_add"})

print("")
print("-----Data Setelah Diupdate-----")

print(data_dict.get('key1'))
print(data_dict.get('key2'))
print(data_dict.get('key3'))
print(data_dict.get('key4'))

print("")
print("-----Menghapus Data-----")
# ini bisa
data_dict.pop("key4")
print("dictionary dihapus ->",data_dict.get('key4'))

# ini bisa juga
del data_dict["key1"]
print("dictionary dihapus ->",data_dict.get('key1'))

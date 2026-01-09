# copy dictionary

teman_teman = {
    "t1": "michael",
    "t2": "gama",
    "t3": "lambok",
    "t4": "ferdi",
    "t5": "hizkia"
}

teman = teman_teman.copy()
print("-----Dict Asli-----")
items = teman_teman.items()
keys  =teman_teman.keys() 
values=teman_teman.values()
for keys,values in items:
    print(keys,"->",values)

print("-----Dict Copy-----")
items = teman.items()
for keys,values in items:
    print(keys,"->",values)

# cek addres with hex
print("-----Address-----")
print("teman_teman:",hex(id(teman_teman)))
print("teman      :",hex(id(teman)))

# pop dictionary (bisa dianggap menghapus)(bisa juga memindahkan ke var lain)
data_simpan = teman.pop("t1")
print("-----Dict Copy After Pop-----")
items = teman.items()
for keys,values in items:
    print(keys,"->",values)

print(data_simpan)

# popitem dictionary (akan mengambil data terakhir aja)
data_simpan = teman.popitem()
print("-----Dict Copy After Popitem-----")
items = teman.items()
for keys,values in items:
    print(keys,"->",values)

print(data_simpan)
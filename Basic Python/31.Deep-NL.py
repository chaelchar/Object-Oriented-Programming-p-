# Deep coppy Nested List
data_0 = [1,2]
data_1 = [3,4]
data_gabung = [data_0,data_1]
data_coppy  = data_gabung.copy()
print(data_gabung)

# mengambil data dari NL
# mengambil data pertama
data = data_gabung[0]
print("Data pertama ->",data)
# mengambil data pertama + elemen pertama didata pertama
data = data_gabung[0][0]
print("Data pertama + data pertama -> {}".format(data))

print("--List yang dicoppy--")
print(f"Coppy NL -> {data_coppy}")
# Alamatnya
print(f"Alamat cp    -> {hex(id(data_coppy))}")
print(f"Alamat asli  -> {hex(id(data_gabung))}")
# Alamatnya si member-1
print("--Alamat Member List yang dicoppy--")
print(f"Alamat cp    -> {hex(id(data_coppy[0]))}")
print(f"Alamat asli  -> {hex(id(data_gabung[0]))}")\

# deepcopy
from copy import deepcopy
copy = deepcopy(data_gabung)
print(f"Alamat si coppy {hex(id(copy))}")
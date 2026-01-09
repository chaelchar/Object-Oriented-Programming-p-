# pop() --> menghapus data paling akhir
# remove() --> menghapus data berdasarkan value
# insert() --> menyisipkan data ke dalam list
# del --> menghapus data berdasarkan index
# clear() --> menghapus semua data di dalam list

# cara untuk menambahkan
# append() --> menambahkan data di akhir list
# insert() --> menyisipkan data ke dalam list
# extend() --> menambahkan data list dengan list lainnya di akhir list


## operasi
# list == index == 0 1 2 3 dst....
data = ["michael","kael","wanen"]

# mengambil data dari list
# index 0
data_0 = data[0]
print(data_0)
# index 1
data_1 = data[1]
print(data_1)
# index 2
data_2 = data[-1]
print(data_2)

# mengambil panjang
print(f"panjang list :{len(data)}")

print("")
 
## Manipulasi data list
# menambahkan item pada list
print(f"data sebelum ditambah\n-->{data}")

data.insert(1,"wannen") # insert = menambah bebas dimana saja
print(f"data sesudah ditambah\n-->{data}")

data.append("michael") # append = menambah pada akhir list
print(f"listnya : {data}")

# menambahkan list dengan list
data_baru = ['lambok','bokk','lambokbok']

data.extend(data_baru) # menggabungkan 2 list (gabungan)
print(data)

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(data)

# meremove data
data.remove("Michael")
print(data)
data.remove("michael")
data.remove("wannen")
print(data)

# meremove data paling belakang
diambil = data.pop()
print(f"data akhir :{data}")
print(f"yang diambil :{diambil}")
 
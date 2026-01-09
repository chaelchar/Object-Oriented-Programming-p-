# Lambda function

def kuadrat(angka):
    '''--fungsi biasa--'''
    return angka**2

print(f"hasil kuadrat -> {kuadrat(3)}")

# Lambda
# output = lambda argument: expresion
kuadrat = lambda angka:angka**2
print(f"lambda kuadrat -> {kuadrat(5)}")

# def pangkat(num,pow):
#     return num**pow

pangkat = lambda num,pow : num**pow
print(f"hasil pangkat num pow -> {pangkat(4,2)}")

## kegunaan

# sorting for list
data_list = ['lambo','ferdi','hizkia']
data_list.sort()
print(f"sorted list -> {data_list}")
# diurutkan berdasarkan jumlah karakternya (panjang)

data_list.sort(key=len)
print(f"sorted list by len -> {data_list}")

# dengan fungsi
def panjang_nama(nama):
    return len(nama)

list_nama = ['mikael','lambok','ferdi','hizkia']
list_nama.sort(key=panjang_nama)
print(f"fungsi panjang nama -> {list_nama}")

# menggunakan lambda
del panjang_nama,list_nama

list_nama = ['elektro','komputer','informatika','rekayasa']
list_nama.sort(key=lambda nama:len(nama))
print(f"panjang dengan lambda -> {list_nama}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10]

def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)

# lambda
data = list(filter(lambda x:x<=5,data_angka)) 
print(f"data angka -> {data}")

# anonymouse function
print("")
print("")

# currying <-- Haskell Curry (yang membuat haskel)
def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print("Fungsi biasa ->",data_hasil)

# lambda
def pangkat(n):
    return lambda x:x**n

pangkat_2 = pangkat(2)
print(f"lambda 5 pangkat 2 -> {pangkat_2(5)}")

# alternatif
def pangkat(x):
    return lambda y:y**x
print(f"hasil pangkat -> {pangkat(3)(3)}")

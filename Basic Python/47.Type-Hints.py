# type hint --> mencegah kita memasukan tipe data yang berbeda pada suatu fungsi
# contoh    --> fungsi(data)  -> data(int)
# inputan fungsi('string') -> ini akan mengakibatkan error

'''-----STUDI KASUS-----'''
def fungsi(nilai):
    hasil = nilai**2
    return hasil

print(fungsi(2)) #--> benar
# print(fungsi('thomas')) --> salah

# SOlusinya memakai type hint
def function(nilai:int):
    print(f"nilai --> {nilai}")

# arti -> nilai:int -> note || tidak ada tipe data return pengembalian
function(2)

def function_2(nilai:int)->int:
    hasil = print(f"hasil jumlah 2 -> {nilai+2}")
    return hasil

# arti -> nilai:int -> int || tipe data returnnya integer
function_2(4)

def function_3(hello:str,name:str):
    print(f"hasil -:> {hello} {name}")
function_3('apakabar','michael')
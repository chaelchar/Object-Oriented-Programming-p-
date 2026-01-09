'''---*Args---'''

# memasukan data/argument
def fungsi(nama,tinggi,berat):
    print(f"-----FUNGSI BIASA-----")
    print(f"Nama   -> {nama}")
    print(f"tinggi -> {tinggi}")
    print(f"berat  -> {berat}")
    print(" ")

fungsi('lambok',170,50)

def fungsi(data_list):
    print(f"-----FUNGSI LIST-----")
    data   = data_list.copy()
    nama   = data[0]
    tinggi = data[1]
    berat  = data[2]
#-------------------------------
    print(f"Nama   -> {nama}")
    print(f"tinggi -> {tinggi}")
    print(f"berat  -> {berat}")
    print(" ")

fungsi(['lambok',179,60])

def fungsi(*args):
    print(f"-----FUNGSI ARGS-----")
    nama   = args[0]
    tinggi = args[1]
    berat  = args[2]
#-------------------------------
    print(f"Nama   -> {nama}")
    print(f"tinggi -> {tinggi}")
    print(f"berat  -> {berat}")
    print(" ")

fungsi('lambok',170,50)

def num(*args):
    # data tipenya -> tuple, dia bisa di-iterasi
    output = 0
    for sum in args:
        output += sum
    return output
list = num(1,2,3,4,5,6,7,8,9,10)
print(f"result -> {list}")
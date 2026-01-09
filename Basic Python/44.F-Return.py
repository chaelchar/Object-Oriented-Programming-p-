'''Fungsi dengan kembalian'''

def kuadrat(angka):
    '''Fungsi kuadrat'''
    output = angka**2
    return output

y = kuadrat(5)
print(f"hasil kuadrat -> {y}")

z = 10 + kuadrat(3)
print(f"hasil {10} + {kuadrat(3)} -> {z}")

def tambah(ak_1,ak_2):
    return ak_1 + ak_2

A = tambah(10,8)
print(f"Hasil -> {A}")

# fungsi dengan multi return

def hitung(ak_1,ak_2):
    tambah = ak_1 + ak_2
    kali   = ak_1 * ak_2
    kurang = ak_1 - ak_2
    bagi   = ak_1 / ak_2
    return tambah,kali,kurang,bagi

T,KA,KU,B = hitung(10,5)
print(f"hasil tambah -> {T}")
print(f"hasil kali   -> {KA}")
print(f"hasil kurang -> {KU}")
print(f"hasil bagi   -> {B}")

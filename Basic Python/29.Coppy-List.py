## mengcoppy list
a = ['elektro','metalurgi','informatika']
print(f"a = {a}")
b = a
print(f"b = {b}")
# merubah a -- merubah b
# merubah b -- merubah a

# memory a dan b
print(f"alamat a {hex(id(a))}")
print(f"alamat b {hex(id(b))}")
# disini, alamat si a dan b itu sama
# jadi nilainya nanti itu sama

# Duplikat List

c = a.copy()
print("c = ",c)
print(f"alamat c {hex(id(c))}")
# alamat si c sudah berbeda


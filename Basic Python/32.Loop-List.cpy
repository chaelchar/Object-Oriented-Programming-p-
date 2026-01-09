# Looping dari list

# for loop
kumpulan_angka = [4,3,2,1,3,2]
print("")
print("-----For Loop-----")
for angka in kumpulan_angka:
    print(f"loop angka ->{angka}")

kumpulan_nama = ["Alice", "Bob", "Charlie"]
print("")
print("-----For Loop-----")
for nama in kumpulan_nama:
    print(f"loop nama -> {nama}")

angka = [4, 3, 2, 1, 3, 2]
print("")
print("-----For Loop-----")
for i in range(len(angka)):
    print(f"loop angka[{i}] -> {angka[i]}")

# while
print("")
print("-----While Loop-----")
i = 0
while i < len(angka):
    print(f"loop angka[{i}] -> {angka[i]}")
    i += 1

# List comprehension
print("")
print("-----List Comprehension-----")
[print(f"loop angka[{i}] -> {angka[i]}") for i in range(len(angka))]

# enumerate
print("")
print("-----Enumerate-----")
for i, val in enumerate(angka):
    print(f"loop angka[{i}] -> {val}")

# sikit lagi
angka = [1,2,3,4,5]
angka_kuadrat = [i**2 for i in angka] 

print("")
print("-----List Comprehension v2-----")
print(angka)
print(angka_kuadrat)

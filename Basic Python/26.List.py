## --List--

# kumpulan data numbers
data_angka = [1,5,4,2,3]
print(data_angka)

# kumpulan data string
data_string = ['michael','kael','chael']
print(data_string)

# kumpulan boolean
data_boolean = [True,False,True,False]
print(data_boolean)

# kumpulan data campuran
data_campuran = [True, False,1,0,"True"]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(f"data -->{list(data_range)}")

# membuat list dengan for loop, list comprehension

# list biasa
list_for = [i for i in range(0,10)]
print(list_for)
# pangkat 2
list_for = [i**2 for i in range(0,10)]
print(list_for)

# membuuat list pake for pake if
# tidak sama dengan
list = [i for i in range(0,10) if i!= 5]
print(list)

# genap
list = [i for i in range(0,10) if i%2 ==0]
print(list)

# ganjil
list = [i for i in range(0,10) if i%2 == 1]
print(list)

# Dictionary

# List -> array kita mengakses dengan menggunakan index
# Dictionary -> object kita mengakses dengan menggunakan key (identifier)

# dictionary -> associative array

data_dict = {
    "key1": "John",
    "key2": "anddre",
    "key3": "Thomas"
}

print("dict-1 ->",data_dict['key1'])
print("dict-2 ->",data_dict['key2'])
print("dict-3 ->",data_dict['key3'])

print("")

list = ["nama_1", "nama_2", "nama_3"]



dict = {
    "key1": list[0],
    "key2": list[1],
    "key3": list[2],
    "key4": list,
    "key5": data_dict
}

print("dict-1 ->",dict["key1"])
print("dict-2 ->",dict["key2"])
print("dict-3 ->",dict["key3"])
print("dict-4 ->",dict["key4"])
print("dict-5 ->",dict["key5"])
# a = 10
# a adalah variabel dengan nilai 10

# int
a = 10
print("data = ", a, "bertipe = ", type(a))

# float
a = 2.5
print("data = ", a, "bertipe = ", type(a))

# string
a = "Kalimat"
print("data = ", a, "bertipe = ", type(a))

# boolean
a = True
b = False
print("data = ", a, "bertipe = ", type(a))
print("data = ", b, "bertipe = ", type(b))

# kompleks
a = complex(5,6)
print("data = ", a, "bertipe = ", type(a))

# Tipe Data bahasa c
from ctypes import c_double, c_char
# double = float || koma-koma
a = c_double(2.5)
print("data = ", a, "bertipe = ", type(a))
# char = karakter

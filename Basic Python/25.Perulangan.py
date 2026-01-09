# Latihan perulangan membaut segitiga

S = 5
C = 1
for i in range(S):
    print("*"*C)
    C += 1 

H = 1
while True:
    print("*"*H)
    H+=1
    if H > S:
        break

# 1. menampilkan yg genap aja
# 2. menampilkan yg ganjil aja

# genap 
A = 1
while 1:
    if A%2:
        A += 1
        continue
    else:
        print("*"*A)
        A += 1
    if A > 10:
        break

# itu yg genap aja

B = 1
while 1:
    if A%2:
        print("*"*B)
        B += 1
    else:
        B += 1
        continue # balik ke atas
 



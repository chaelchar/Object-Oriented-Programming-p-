angka = 0
while angka <= 10:
    angka += 1
    print(f"-->{angka}")

    if angka == 5:
        print(5*"-")
        break
    
    print(5*"+")


num = int(input("input batas angka : "))
start = 0
while True:
    start += 1
    print(f"-->{start}")
    if start == num:
        break

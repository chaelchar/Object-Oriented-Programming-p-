# continue, pass, break
angka = 0
while True:
    print(f"angka --> {angka}")
    angka += 1
    if angka == 5:
        break

print("Program pertama\n")

number = 0
while number <= 10:
    print(f"number :{number}")
    number += 2
    if number == 4:
        pass

print("Program kedua\n")

num = 0
while num <= 10:
    num += 1
    print(f"--> {num}")
    if num == 5:
        print("+++++++")
        continue # ngeskip code dibawahnya, akan loncat keawal loop
    print("---------")
'''-----**Kwargs-----'''

def fungsi(nama,nim,prodi):
    print(f"-----FUNGSI BIASA-----")
    print(f"Nama  -> {nama}")
    print(f"Nim   -> {nim}")
    print(f"Prodi -> {prodi}")
    print(" ")

fungsi('michael','13S24037','Elektro')

def nama(nama:str,tinggi:int,berat:int):
    '''fungsi biasa'''
    print(f"nama -> {nama}\ntinggi -> {tinggi}\nberat ->{berat}")

nama('michael',180,80)

print(" ")

def fungsi(**kwargs):
    nama = kwargs['nama']
    nim = kwargs['nim']
    prodi = kwargs['prodi']
    
    print(f"nama  -> {nama}")
    print(f"nim   -> {nim}")
    print(f"prodi -> {prodi}")

fungsi(nama= 'michael',nim='13S24037',prodi='Teknik Elektro')

def math(*args,**kwargs):
    print("-----input operator-----")
    print("1.tambah\n2.kali\n3.jumlah-pangkat")
    user = int(input("input operator -> "))
    if kwargs['A'] == user:
        output = 0
        for i in args:
            output+= i
        return output
    elif kwargs['B'] == user:
        output = 1
        for i in args:
            output *= i
        return output
    elif kwargs['C'] == user:
        output = 0
        for i in args:
            output += i**2
        return output
    else:
        print("-----Eror-----")


hasil = math(1,2,3,4,5,A=1,B=2,C=3)
print(f"Hasil -> {hasil}")

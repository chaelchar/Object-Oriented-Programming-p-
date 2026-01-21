class Student:
    def __init__(self, nama, ipk):
        self.nama = nama
        self.ipk = ipk

    def cetak_info(self):
        print("Nama:", self.nama, "| IPK:", self.ipk)


class Course:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, student):
        if len(self.daftar_mahasiswa) < self.kapasitas:
            self.daftar_mahasiswa.append(student)
        else:
            print("Kapasitas penuh!")

    def cetak_semua_mahasiswa(self):
        print("Jumlah Mahasiswa:", len(self.daftar_mahasiswa))
        for mhs in self.daftar_mahasiswa:
            mhs.cetak_info()


# Inisialisasi mahasiswa
m1 = Student("Boboiboy", 4.0)
m2 = Student("Fang", 4.0)
m3 = Student("Gopal", 3.0)
m4 = Student("Ying", 3.0)
m5 = Student("Yaya", 3.0)

# Inisialisasi mata kuliah
matkul = Course(kapasitas=10)

# Tambah mahasiswa ke course
matkul.tambah_mahasiswa(m1)
matkul.tambah_mahasiswa(m2)
matkul.tambah_mahasiswa(m3)
matkul.tambah_mahasiswa(m4)
matkul.tambah_mahasiswa(m5)

# Tampilkan semua mahasiswa
matkul.cetak_semua_mahasiswa()

class Karyawan:
    def __init__(self, nama, nomor, tgl_lahir, tgl_rekrut):
        self._nama = nama
        self._nomor = nomor
        self._tgl_lahir = tgl_lahir
        self._tgl_rekrut = tgl_rekrut

    def tampilkan_data(self):
        print("Nama               :", self._nama)
        print("Nomor Karyawan     :", self._nomor)
        print("Tanggal Lahir      :", self._tgl_lahir)
        print("Tanggal Rekrut     :", self._tgl_rekrut)


class KaryawanTetap(Karyawan):
    BONUS_PERSEN = 5.0   # 500%

    def __init__(self, nama, nomor, tgl_lahir, tgl_rekrut, gaji_bulanan):
        super().__init__(nama, nomor, tgl_lahir, tgl_rekrut)
        self.gaji_bulanan = gaji_bulanan

    def bonus_tahunan(self):
        return self.gaji_bulanan * self.BONUS_PERSEN

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Gaji Bulanan       :", self.gaji_bulanan)
        print("Bonus Tahunan      :", self.bonus_tahunan())


class KaryawanPerJam(Karyawan):
    TARIF_LEMBUR = 0.5   # 50%

    def __init__(self, nama, nomor, tgl_lahir, tgl_rekrut, upah_per_jam):
        super().__init__(nama, nomor, tgl_lahir, tgl_rekrut)
        self.upah_per_jam = upah_per_jam

    def tarif_lembur(self):
        return self.upah_per_jam * self.TARIF_LEMBUR

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Upah Per Jam       :", self.upah_per_jam)
        print("Tarif Lembur/Jam   :", self.tarif_lembur())


# Inisialisasi objek
print("=== KARYAWAN TETAP ===")
kt = KaryawanTetap("Budi", "14221", "14-Jan-2008", "10-Mar-2026", 500)
kt.tampilkan_data()

print("\n=== KARYAWAN PER JAM ===")
kpj = KaryawanPerJam("Tony", "1224", "15-Okt-2006", "15-Jan-2026", 300)
kpj.tampilkan_data()

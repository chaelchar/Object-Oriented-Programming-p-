class BujurSangkar:
    def __init__(self, sisi):
        self._sisi = sisi   # protected attribute
    
    def keliling(self):
        return 4 * self._sisi

    def luas(self):
        return self._sisi * self._sisi


class Kubus(BujurSangkar):
    def __init__(self, sisi):
        super().__init__(sisi)

    def luas_kubus(self):
        return 6 * self._sisi * self._sisi

    def volume_kubus(self):
        return self._sisi ** 3


# Inisialisasi objek
persegi = BujurSangkar(2)
print("Keliling Persegi:", persegi.keliling())
print("Luas Persegi:", persegi.luas())

print()

kubus = Kubus(2)
print("Luas Kubus:", kubus.luas_kubus())
print("Volume Kubus:", kubus.volume_kubus())

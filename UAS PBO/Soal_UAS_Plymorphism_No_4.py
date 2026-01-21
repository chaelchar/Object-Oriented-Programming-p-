class Account:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def deposit(self, jumlah):
        self.saldo += jumlah
        print("Deposit berhasil")

    def withdraw(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print("Penarikan berhasil")
        else:
            print("Saldo tidak cukup")

    def info(self):
        print("Nama  :", self.nama)
        print("Saldo :", self.saldo)


class SavingsAccount(Account):
    def __init__(self, nama, saldo, bunga):
        super().__init__(nama, saldo)
        self.bunga = bunga   # contoh: 0.05 = 5%

    def add_interest(self):
        bunga = self.saldo * self.bunga
        self.saldo += bunga
        print("Bunga ditambahkan:", bunga)


class CheckingAccount(Account):
    def __init__(self, nama, saldo, biaya_transaksi):
        super().__init__(nama, saldo)
        self.biaya_transaksi = biaya_transaksi

    def withdraw(self, jumlah):
        total = jumlah + self.biaya_transaksi
        if total <= self.saldo:
            self.saldo -= total
            print("Penarikan + biaya berhasil")
        else:
            print("Saldo tidak cukup untuk biaya transaksi")

print("=== ACCOUNT ===")
a = Account("Amato", 200000)
a.info()
a.deposit(50000)
a.withdraw(30000)
a.info()

print("\n=== SAVINGS ACCOUNT ===")
s = SavingsAccount("Clamcabot", 50000, 0.2)
s.info()
s.add_interest()
s.info()

print("\n=== CHECKING ACCOUNT ===")
c = CheckingAccount("Kaizo", 40000, 2000)
c.info()
c.withdraw(10000)
c.info()

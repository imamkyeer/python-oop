
class User:
    def __init__(self,nama: str, username: str, password: str):
        self.nama = nama
        self.username = username
        self.__password = password

    def cek_password(self, password: str) -> bool:
        return self.__password == password


class Admin(User):
    def __init__(self, nama: str, username: str, password: str):
        super().__init__(nama, username, password)

    def info(self):
        print("👑 Masuk Sebagai Admin")


class BankAccount:
    def __init__(self, nama: str, nis: str,saldo_awal: int ):
        self.nama = nama
        self.nis = nis
        self.__saldo = saldo_awal

    def get_saldo(self)-> int:
        return self.__saldo
    
    def setor(self, jumlah: int)-> None:
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"✅ Setor berhasil: {jumlah}")
        else:
            print("⚠️ setor uang gagal!!!")

    def tarik(self, jumlah: int) -> None:
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"✅ Tarik berhasil: {jumlah}")
        else:
            print("❌ Saldo tidak cukup")


class Santri(User):
    def __init__(self, nama: str, username: str, password: str, nis: str):
        super().__init__(nama, username, password)
        self.nis = nis
        self.rekening = BankAccount(nama, nis, 0)


data_santri = []

s = Santri("Imam", "imssy_sans", "09212009", "001")
s.rekening.setor(150000)
data_santri.append(s)

def input_int(pesan: str) -> int:
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("❌ Harus angka!")


def menu_santri(santri: Santri):
    while True:
        print("\n=== MENU TABUNGAN === ")
        print("1. Cek saldo")
        print("2. Setor tunai")
        print("3. Tarik tunai")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            print("💰 Saldo:", santri.rekening.get_saldo())

        elif pilihan == "2":
            jumlah = input_int("Jumlah setor: ")
            santri.rekening.setor(jumlah)

        elif pilihan == "3":
            jumlah = input_int("Jumlah tarik: ")
            santri.rekening.tarik(jumlah)

        elif pilihan == "0":
            print("👋 Keluar...")
            break
        else:
            print("❌ Menu tidak valid")


    while True:
        print("\n=== TABUNGAN DIGITAL SANTRI ===")
        print("1. Daftar Santri")
        print("2. Login Santri")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            nama = input("Nama: ")
            username = input("Username: ")
            password = input("Password: ")
            nis = input("NIS: ")

            santri = Santri(nama, username, password, nis)
            data_santri.append(santri)
            print("✅ Pendaftaran berhasil!")

        elif pilih == "2":
            username = input("Username: ")
            password = input("Password: ")

            ditemukan = False
            for santri in data_santri:
                if santri.username == username and santri.cek_password(password):
                    print(f"✅ Login berhasil. Selamat datang {santri.nama}")
                    menu_santri(santri)
                    ditemukan = True
                    break

            if not ditemukan:
                print("❌ Login gagal")

        elif pilih == "0":
            print("👋 Program selesai")
            break
        else:
            print("❌ Menu tidak valid")

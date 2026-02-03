
data = [
    {"id": 1, "nama": "imam", "kelas": "x-b"},
    {"id": 2, "nama": "ronaldo1", "kelas": "x-b"}
]

def tambah_data():
    id = int(input("Masukan ID: "))
    nama = input("Masukan nama: ")
    kelas = input("Masukan kelas: ")

    data.append({
        "id": id,
        "nama": nama,
        "kelas": kelas
    })

def tampil_data():
    for d in data:
        print(d["id"], d["nama"], d["kelas"])

def ubah_data():
    id = int(input("Masukan ID yang mau diubah: "))
    for d in data:
        if d["id"] == id:
            d["nama"] = input("Nama baru: ")
            d["kelas"] = input("Kelas baru: ")
            print("Data berhasil diubah")
            return
    print("ID tidak ditemukan")

def hapus_data():
    id = int(input("Masukan ID yang mau dihapus: "))
    for d in data:
        if d["id"] == id:
            data.remove(d)
            print("Data berhasil dihapus")
            return
    print("ID tidak ditemukan")

while True:
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak valid")
        break







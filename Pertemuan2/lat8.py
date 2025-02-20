class Pelajar:
    def __init__(self, nama, absen): #konstruktor
        self.nama = nama
        self.absen = absen

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Absen: {self.absen}")

pelajar1 = Pelajar("Andi", "18")
pelajar1.tampilkan_info()
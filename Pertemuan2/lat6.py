class manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def cetak(self):
        print("Nama : " + self.nama)
        print("Umur : " + self.umur)

nama = input("Masukkan nama : ")
umur = input("Masukkan umur : ")

manusia = manusia(nama, umur)
manusia.cetak()
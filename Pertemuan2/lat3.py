class persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi*self.sisi

    def keliling(self):
        return self.sisi*4

sisi = int(input("Masukkan sisi persegi : "))
persegi = persegi(sisi)

print(f"Keliling : {persegi.keliling()}")
print(f"Luas : {persegi.luas()}")
class menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

menu1 = menu("Nasi goreng", 15000)

print("Menu : " + menu1.nama)
print("Harga : " + str(menu1.harga))

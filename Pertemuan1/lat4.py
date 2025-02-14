angka = int(input("Masukkan angka yang akan dicek : "))
if angka < 2:
    print("Bukan angka prima!")
else:
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            print("Bukan angka prima")
            break
        else:
            print("Adalah angka prima")
            break
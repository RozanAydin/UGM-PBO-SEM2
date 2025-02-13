while True:
    try:
        angka = int(input("Masukkan angka: "))
        for i in range(angka + 1):
            print(angka, end = " ")
            angka = angka - 1
        break
    except:
        print("masukkan dalam bentuk angka!")

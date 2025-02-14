suhu = float(input("Masukkan nilai suhu (dalam derajat Celcius): "))

if suhu <= 0:
    print("Membeku")
elif suhu <= 10:
    print("Sangat Dingin")
elif suhu <= 20:
    print("Sejuk")
elif suhu <= 30:
    print("Hangat")
else:
    print("Panas")
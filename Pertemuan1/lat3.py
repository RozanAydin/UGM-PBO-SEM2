niu = int(input("Masukkan NIU : "))
tugas = int(input("Masukkan nilai tugas : "))
laporan = int(input("Masukkan nilai laporan : "))

rata2 = (tugas + laporan) // 2
if rata2 <= 40:
    print("Nilai anda : K")
else:
    ujian = int(input("Masukkan nilai ujian : "))
    nilai_akhir = (0.25 * tugas) + (0.25 * laporan) + (0.5 * ujian)
    if 80 <= nilai_akhir <= 100:
        nilai_huruf = "A"
    elif 70 <= nilai_akhir < 80:
        nilai_huruf = "B"
    elif 60 <= nilai_akhir < 70:
        nilai_huruf = "C"
    elif 50 <= nilai_akhir < 60:
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"
    print(f"Nilai anda : {nilai_huruf}")
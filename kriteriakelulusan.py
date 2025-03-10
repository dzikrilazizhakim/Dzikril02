def cek_kelulusan(bayar_semester, rata_rata_ujian):
    if bayar_semester.lower() == 'y' and rata_rata_ujian.lower() == 'y' :
        return "Lulus"
    else:
        return "tidak lulus"
    
bayar_semester = input("apakah sudah full bayar semester (y/n): ")
rata_rata_ujian = input("apakah mengikuti ujian dengan rata-rata C atau lebih (y/n): ")

hasil = cek_kelulusan(bayar_semester, rata_rata_ujian)
print("hasil ", hasil)
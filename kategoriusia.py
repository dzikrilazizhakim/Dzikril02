def kategori_usia(usia):
    if usia < 0 :
        return "usia tidak tentu"
    elif usia <= 2:
        return "Bayi"
    elif usia <= 5:
        return "Balita"
    elif usia <= 12:
        return "Anak-anak"
    elif usia <= 18:
        return "Remaja"
    else:
        return "Dewasa"
    
usia = float(input("masukkan usia dalam tahun: "))
kategori = kategori_usia(usia)
print(f"kategori usia: {kategori}")

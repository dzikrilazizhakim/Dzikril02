def hitung_nilai_matapelajaran(Matematika, Saint, Inggris):
    rata_rata = (Matematika + Saint + Inggris) / 3
    di_bawah_70 = sum(1 for nilai in [Matematika, Saint, Inggris] if nilai < 70)

    if rata_rata > 75 and di_bawah_70 <= 1:
        return "Lulus"
    else: 
        return "Tidak Lulus"
    
Matematika = float(input("masukkan nilai matematika: "))
Saint = float(input("masukkan nilai saint:"))
Inggris = float(input("masukkan nilai inggris: "))

hasil = hitung_nilai_matapelajaran(Matematika, Saint, Inggris)
print(f"hasil: {hasil}")
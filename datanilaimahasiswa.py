# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (0.3 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas)
    return nilai_akhir


jumlah_mahasiswa = int(input("Berapa banyak mahasiswa? "))


daftar_mahasiswa = []

for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    
   
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    
    
    mahasiswa = {
        'nama': nama,
        'nim': nim,
        'nilai_akhir': nilai_akhir
    }
    daftar_mahasiswa.append(mahasiswa)

# Tampilkan hasil
print("\nData Mahasiswa dan Nilai Akhir:")
print("--------------------------------")
for mahasiswa in daftar_mahasiswa:
    print(f"Nama: {mahasiswa['nama']}")
    print(f"NIM: {mahasiswa['nim']}")
    print(f"Nilai Akhir: {mahasiswa['nilai_akhir']:.2f}")
    print("--------------------------------")

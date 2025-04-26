total_detik = int(input("masukkan total detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print ("\n=== Hasil Konversi ===")
print ("Jam        :", jam)
print ("Sisa Detik :", sisa_detik)
print ("Menit      :", menit)
print ("Detik      :", detik)
print ("==================")
alas = int(input("Masukkan panjang alas segitiga: "))
tinggi = int(input("Masukkan tinggi segitiga: "))
luas = alas * tinggi // 2 
sisi_miring = (alas**2 + tinggi**2) * 0.5
keliling = int(alas + tinggi + sisi_miring)
print("Luas segitiga =", luas)
print("Keliling segitiga =", keliling)
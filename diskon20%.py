harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah uang: "))
diskon = 0.2 
total = harga - int(harga * diskon)  
kembalian = jumlah - total
print("Total harga setelah diskon = Rp", total)
print("Uang kembalian = Rp", kembalian)
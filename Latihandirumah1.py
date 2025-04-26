nama_barang = input("masukkan nama barang: ")
harga_satuan_barang = int(input("masukkan harga satuan barang: "))
jumlah_yang_dibeli = int(input("masukkan jumlah yang dibeli: "))

total_bayar = (harga_satuan_barang * jumlah_yang_dibeli)

print ("\n=== STRUK PEMBAYARAN ===")
print (f"nama barang: {nama_barang}")
print (f"harga satuan barang: RP{harga_satuan_barang:,}")
print (f"jumlah yang dibeli: {jumlah_yang_dibeli}")
print (f"total bayar: RP{total_bayar:,}")
print ("==================")


def hitung_total_bayar(total_belanja):
    if total_belanja > 100000:
        diskon = 0.10
    elif total_belanja > 50000:
        diskon = 0.5
    else:
        diskon = 0.0

    total_diskon = total_belanja * diskon
    total_bayar = total_belanja - total_diskon
    return total_bayar

total_belanja = float(input("Masukkan Total Belanja: "))
total_bayar = hitung_total_bayar(total_belanja)
print(f"total yang harus di bayarkan setelah diskon: {total_bayar}")
    
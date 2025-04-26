bilangan1 = int(input(" masukkan bilangan pertama: "))
operator = input(" masukkan operator(+, -, *, /): ")
bilangan2 = int(input(" masukkan bilangan kedua: "))

if operator == "+":
    hasil = bilangan1 + bilangan2
elif operator == "-":
    hasil = bilangan1 - bilangan2
elif operator == "*":
    hasil = bilangan1 * bilangan2
elif operator == "/":
    if bilangan2 != 0:
        hasil = bilangan1 // bilangan2
    else:
        hasil = "error: tidak bisa dibagi dengan nol."
else:
    hasil = "operator tidak valid."
    
print ("\n=== HASIL ===")
print ("Hasil :", hasil)
print("====================")
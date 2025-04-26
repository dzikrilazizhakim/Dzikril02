angka1 = float(input("masukkan angka pertama: "))
operator = input("masukkan operator(+, -, *, /): ")
angka2 = float(input("masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "error: pembagian dengan nol tidak diperbolehkan."
else:
    hasil = "operator tidak dikenali."
    
print ("\n=== Hasil Kalkulator ===")
print ("Hasil:", hasil)
print ("==================")
bilangan1 = int(input("masukkan bilangan pertama: "))
operator = (input("masukkan operator (+, -, *, /) "))
bilangan2 = int(input("masukkan bilangan kedua: "))

if operator == "+":
    hasil = bilangan1 + bilangan2
elif operator == "-":
    hasil = bilangan1 - bilangan2
elif operator == "*":
    hasil = bilangan1 * bilangan2
elif operator == "/":
     hasil = bilangan1 / bilangan2
else:
    hasil = ("operasi tidak dikenali.")

print ("Hasil:", hasil) 
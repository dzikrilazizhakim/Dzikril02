while True:

    bilangan1 = float(input("masukkan bilangan pertama: "))
    bilangan2 = float(input("masukkan bilangan kedua: "))
    operator = input("masukkan operator (+, - , *, /): ")

    if operator == "+":
        hasil = bilangan1 + bilangan2
    elif operator == "-":
        hasil = bilangan1 - bilangan2
    elif operator == "*":
        hasil = bilangan1 * bilangan2
    elif operator == "/":
        hasil = bilangan1 / bilangan2
    else:
        hasil = "operator tidak valid."

    print ("Hasil", hasil)

    lanjut = input("Mau Lanjut? (y/n), ")
    if lanjut.lower() != "y":
        break
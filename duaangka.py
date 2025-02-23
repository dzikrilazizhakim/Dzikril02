operator = input('Pilih operator: "penambahan", "pengurangan", "perkalian", "pembagian": ')
angka1 = int(input("Masukkan angka pertama: "))  
angka2 = int(input("Masukkan angka kedua: "))
if operator == 'penambahan':
    hasil = angka1 + angka2
elif operator == 'pengurangan':
    hasil = angka1 - angka2
elif operator == 'perkalian':
    hasil = angka1 * angka2
elif operator == 'pembagian':
    hasil = angka1 / angka2
else:
    print("Operator tidak valid.")
    hasil = None  
if hasil is not None:
    print(f'Hasil {operator} dari {angka1} dan {angka2} adalah {hasil}')
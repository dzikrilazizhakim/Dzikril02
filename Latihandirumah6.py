nilai = int(input("masukkan nilai ujian: "))

if nilai >= 90 and nilai <=100:
    print("Grade: A")
elif nilai >= 80 and nilai <= 89:
    print("Grade: B")
elif nilai >= 70 and nilai <= 79:
    print("Grade: C")
elif nilai >= 60 and nilai <= 69:
    print("Grade: D")
elif nilai < 60:
    print("Grade: E")
else: 
    print("nilai tidak valid")
    
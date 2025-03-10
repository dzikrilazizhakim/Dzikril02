kategori = input("jenis kendaraan (mobil/motor) :")
value = input("berapa nilai NJKB: ")
firstvehicle = input("apakah ini kendaraan pertama? (ya/tidak): ")
pkb = 2/100*value
final = 0

if (firstvehicle == "tidak"):
    numberVehicle = int(input("kendaraan keberapa ini (-20)"))
    pkb = (2 + (numberVehicle -1) * 0.5)/100 * value
    
if (category == "mobil"):
    final = pkb + 143000
    
    
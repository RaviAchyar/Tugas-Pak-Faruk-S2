# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

# ELIF
 
# Input usia dari pengguna
usia = int(input("Masukkan usia Anda: "))

# Menentukan kategori usia
if usia >= 0 and usia <= 12:
    print("Kategori Usia Anda: Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Kategori Usia Anda: Remaja")
elif usia >= 18 and usia <= 50:
    print("Kategori Usia Anda: Dewasa")
else:
    print("Kategori Usia Anda: Lansia")
print()
print("----------------------------")
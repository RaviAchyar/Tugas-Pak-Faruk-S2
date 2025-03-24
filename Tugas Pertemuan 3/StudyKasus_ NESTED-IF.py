# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

# NESTED IF

# Input usia
usia = int(input("Masukkan usia pembeli: "))

# Menentukan harga tiket
if usia < 10:
    print("Harga tiket Anda: 50.000")
else:
    if usia <= 60:
        print("Harga tiket Anda: 100.000")
    else:
        print("Harga tiket Anda: 70.000")
print()
print('Silahkan datang kembali')
print("----------------------------")
# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

nilai = input("Masukkan nilai (pisahkan dengan koma): ")

hasil = map(lambda n: (
    'A' if int(n) >= 85 else
    'B' if int(n) >= 75 else
    'C' if int(n) >= 65 else
    'D' if int(n) >= 50 else
    'E'
), nilai.split(','))

print("Nilai huruf:", ', '.join(hasil))


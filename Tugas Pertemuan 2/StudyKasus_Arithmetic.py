# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

# Addition
print('---------Penjumlahan---------')
angka1 = int(input('Masukkan Angka1: '))
angka2 = int(input('Masukkan Angka2: '))
sub1 = angka1 + angka2
print('Hasil penjumlahan: ',sub1)
print()

# Subtraction
print('---------Pengurangan---------')
angka3 = int(input('Masukkan Angka1: '))
angka4 = int(input('Masukkan Angka2: '))
sub2 = angka3 - angka4
print('Hasil pengurangan: ',sub2)
print()

# Multiplication
print('---------Perkalian---------')
hasil1 = sub1 * sub2
print('Hasil perkalian', sub1, '*', sub2, '=', hasil1)
print()

# Exponentiation
print('---------Pangkat---------')
print('Masukkan Angka Untuk Pangkat ', hasil1)
pangkat = int(input('Masukkan Angka :'))
total1 = hasil1 ** pangkat
print('Hasil perkalian', hasil1, '**', pangkat, '=', total1)
print()

# Division
print('---------Pembagian---------')
hasil2= sub1 / sub2
print('Hasil perkalian', sub1, '/', sub2, '=', hasil2)
print()

# Floor Divison
print('---------Pembagian kebawah---------')
print('Masukkan Angka Untuk Pembagian kebawah ', hasil2)
floor = int(input('Masukkan Angka :'))
total2 = hasil2 // floor
print('Hasil perkalian', hasil2, '//', floor, '=', total2)
print()

# Modulus
print('---------sisa bagi---------')
sisa = angka1 % angka3
print('Hasil Modulus = ', angka1, '%', angka3, '=', sisa)
print()

# Precedence
print('---------Precedence---------')
full1 = (angka1 * angka3) / (angka2 + angka4)
print('Hasil dari Precedence : ','(', angka1, '*', angka3, ')', '/', '(', angka2, '+', angka4, ')', '=', full1)
print()
full2 = (angka1 + angka3) * (angka2 - angka4)
print('Hasil dari Precedence : ','(', angka1, '+', angka3, ')', '*', '(', angka2, '-', angka4, ')', '=', full2)
print('------------------------------')

# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

# 1. LIST DASAR
belanja = ['Apel', 'Jeruk', 'Pisang']
print("List Awal         :", belanja)
print('-----------------------------')


# 2. ORDERED (urutan tetap)
print("Item pertama      :", belanja[0])
print("Item kedua        :", belanja[1])
print('-----------------------------')

# 3. DUPLICATE (boleh duplikat)
belanja = ['Apel', 'Jeruk', 'Pisang', 'Apel']
print("Duplikat Item     :", belanja)
print('-----------------------------')

# 4. INDEX (cari posisi item)
index_pisang = belanja.index('Pisang')
print("Index 'pisang'      :", index_pisang)
print('-----------------------------')

# 5. CHANGEABLE (bisa diubah)
belanja[1] = 'Mangga'
print("Setelah diubah    :", belanja)
print('-----------------------------')

# 6. TAMBAH DATA
belanja.append('Semangka')
print("Setelah tambah    :", belanja)
print('-----------------------------')

# 7. HAPUS DATA
belanja.remove('Pisang')  # hapus satu 'Pisang'
print("Setelah hapus     :", belanja)
print('-----------------------------')

# 8. EDIT DATA (ubah item tertentu)
belanja[2] = 'Kiwi'
print("Setelah edit item :", belanja)
print('-----------------------------')


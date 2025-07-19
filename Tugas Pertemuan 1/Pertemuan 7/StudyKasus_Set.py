# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

# Buat Set
peserta = {'Dzaky', 'Scendy', 'BIntang', 101}
peserta2 = set(('Dzaky', 'Scendy', 'Rafli', 102))
print("Peserta awal:", peserta)
print("Peserta2 awal:", peserta2)
print('------------------')

# Unordered
print("Urutan tidak dijamin:", peserta)
print('------------------')

# Unduplicatable
peserta.add('Dzaky')
print("Setelah coba tambah duplikat:", peserta)
print('------------------')

# Unindexed
print("Apakah 'BIntang' hadir?", 'BIntang' in peserta)
print('------------------')

# Unchangeable
peserta = {'Dzaky', 'Scendy', 'BIntang', 'Rafli'}
print("Set peserta direset:", peserta)
print('------------------')

# Tambah Data
peserta.add('Lukman')
print("Setelah tambah 'Lukman':", peserta)
print('------------------')

# Hapus Data
peserta.remove('Scendy')
print("Setelah hapus peserta:", peserta)
print('------------------')


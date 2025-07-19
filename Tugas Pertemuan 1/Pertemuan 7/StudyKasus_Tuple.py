# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

# Ordered
nama1 = ('Dzaky', 83)
nama2 = tuple(('Dzaky', 'Scendy'))

print('Data 1     :', nama1)
print('Data 2     :', nama2)
print('---------------------')

# Duplicate
nama1 = ('Dzaky', 83, 83)
nama2 = tuple(('Dzaky', 'Scendy', 'Scendy'))

print('Duplikat 1 :', nama1)
print('Duplikat 2 :', nama2)
print('---------------------')

# Index
Index = nama1.index(83)
print('Index angka 83:', Index)
print('---------------------')

# Unchangeable
try:
    nama1[1] = 90
except TypeError as e:
    print('Error saat mengubah tuple:', e)
print('Hasil Edit :', nama1)
print('---------------------')

# Tupel Python
# koleksi yang terurut, tidak dapat dirubah
my_tuples = ('dian', 'ihsan', 'rosi')
print(my_tuples) # ('dian', 'ihsan', 'rosi')

# satu item, harus diakhiri koma dibelakang
my_tuple = ('nama',)
print(type(my_tuple)) # <class 'tuple'>

# membuat tuple dengan konstruktornya
tupleku = tuple(('rusd', 'diana'))
print(tupleku, type(tupleku))

# Cek jumlah item pada tuple
panjang_tuple = ('saya', 'kamu', 'mereka')
print(len(panjang_tuple)) # 3

# Akses item pada tuple
akses_item = ('ceo', 'manager', 'presdir')
print(akses_item[0])

'''
Tuple tidak dapat diubah, yang artinya tidak dapat diubah, ditambah, atau
dihapus itemnya
'''
# Solusinya yaitu mengkonversi dulu ke List baru ke tuplekan lagi

# Extrak Tuple
fruits = ('apple', 'cherry', 'banana')
(buah1, buah2, buah3) = fruits
print(buah1) # apple
print(buah2) # cherry
print(buah3) # banana

# Extrak Tuple dengan tanda *
color = ('merah', 'kuning', 'hijau', 'biru')
(warna1, *warna2) = color
print(warna1) # merah
print(*warna2) # kuning, hijau, biru

# Iterasi Tuple
umbi = ('kacang', 'kentang', 'lobak')
for item in umbi:
    print(item, end=',') # kacang,kentang,lobak,

print('\n')

for i in range(len(umbi)):
    print(i, umbi[i])

item = 0
while item < len(umbi):
    print(umbi[item])
    item = item + 1
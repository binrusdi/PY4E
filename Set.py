# Set adalah suatu koleksi yang tidak terurut, tidak di index, tidak dapat diubah
# Set dapat diubah dan ditambah
# Akses item set hanya dengan looping

# Menambahkan satu item pada Set
this_set = {
    'mangga', 'jeruk', 'apel'
}
this_set.add('manggis')
print(this_set) # {'jeruk', 'manggis', 'apel', 'mangga'}

# Menambahkan beberapa item pada Set
cars = {'avanza', 'yaris', 'agya'}
colors = {'merah', 'kuning', 'hijau'}
cars.update(colors)
print(cars) # {'hijau', 'yaris', 'agya', 'merah', 'avanza', 'kuning'}

# Menghapus item pada Set
# jika item yang dihapus tidak ada, akan menimbulkan error
remove_set = {'daun', 'ranting', 'dahan'}
remove_set.remove('daun')
print(remove_set)
# jika item yang dihaous tidak ada, tidak akan menimbulkan error
remove_set.discard('buah')
print(remove_set)
# clear() membersihkan item Set
# del menghapus set
# pop() menghapus item terakhir

# Membuat set baru dari penggabunga dua set
set_satu = {'satu', 'dua', 'tiga'}
set_dua = {1, 2, 3}
set_tiga = set_satu.union(set_dua)
print(set_tiga) # {1, 2, 3, 'tiga', 'dua', 'satu'}

# Simpan hanya duplikatnya
# metode intersection-update() <- hanya akan menyimpan item yang ada di kedua set
# metode intersection() <- mengembalikan kumpulan baru, yg hanya berisi item pada ke dua set

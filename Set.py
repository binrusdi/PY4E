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

# Simpan semua, tapi bukan duplikatnya
# symmetric_difference_update() <- hanya akan menyimpan yang tidak ada dikedua set
# symmetric_difference() <- mengembalikan himpunan baru, yang hanya berisi elemen yang TIDAK ada di kedua himpunan.

# Mengembalikan True jika di kedua set tidak ada yang sama
set_mobil = {'propeler', 'balljoin', '4wd'}
set_motor = {'rantai', 'crankshaft', 'gear'}
set_not_item = set_mobil.isdisjoint(set_motor)
print(set_not_item) # True

# Mengembalikan True jika semua item dalam set A ada di set B
x = {'a', 'b', 'c'}
y = {'b', 'a', 'c', 's'}
z = x.issubset(y)
print(z) # True

# atau menggunakan issuperset()
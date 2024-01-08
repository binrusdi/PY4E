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
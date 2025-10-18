# Dict digunakan untuk menyimpan niai data dalam pasangan key:value
# Dict terurut, dapat diubah, dan tidak duplikat
this_dict = {
    'brand': 'toyota',
    'model': 'avanza',
    'tahun': 2015
}
print(this_dict)
# {'brand': 'toyota', 'model': 'avanza', 'tahun': 2015}

# Akses Dict
brand = this_dict['brand']
print(brand)
# toyota

model = this_dict.get('model')
print(model)
# avanza

# Mengembalikan semua key dict
keys = this_dict.keys()
print(keys)
# dict_keys(['brand', 'model', 'tahun'])

# Mendapatkan value dict
values = this_dict.values()
print(values)
# dict_values(['toyota', 'avanza', 2015])

# Mendapatkan item sebagai tuple dalam list
items = this_dict.items()
print(items)
# dict_items([('brand', 'toyota'), ('model', 'avanza'), ('tahun', 2015)])

# Memeriksa key
if 'model' in this_dict:
    print('ya, key model ada di dalam dict')

# Ubah value dict
colors = {
    'terang': 'pink',
    'gelap': 'black'
}
gelap = colors['gelap'] = 'navy'
print(gelap)
# navy

# Memperbaharui item dengan argumen yang diberikan pada update()
component = {
    'break': 'brembo',
    'suspension': 'showa'
}
component.update({'break': 'nissin'})
print(component)
# {'break': 'nissin', 'suspension': 'showa'}

# Menambahkan item ke dict dengan key:value baru
motor = {
    'merk': 'honda',
    'type': 'bebek'
}
motor['warna'] = 'black'
print(motor)
# {'merk': 'honda', 'type': 'bebek', 'warna': 'black'} 

# Menghapus item dict dengan pop('key)
motor.pop('type')
print(motor)
# {'merk': 'honda', 'warna': 'black'} 

# Menghapus item terakhir ditambahkan
motor.popitem()
print(motor)
# {'merk': 'honda'}

# Menghapus key yang ditentukan
motor['tahun'] = 2017
del motor['merk']
print(motor)
# {'tahun': 2017}
# del juga dapat menghapus dict sepenuhnya
# clear() mengkosongkan dict

# Iterasi dict
# key
my_dict = {
  'nama': 'Rusdiana',
  'umur': 29,
  'status': 'Menikah'
}
for dic in my_dict:
  print(dic)

# value
for di in my_dict:
  print(my_dict[di])

# metode values
for value in my_dict.values():
  print(value)

# metode key
for key in my_dict.keys():
  print(key)

# metode items
for item_key, item_value in my_dict.items():
  print(item_key, item_value)
  
# Mengalin dict
my_dict_2 = my_dict.copy()
print(my_dict_2)

my_dict_3 = dict(my_dict)
print(my_dict_3)

# Menyarangkan dict
my_family = {
  'child1' : {
    'name' : 'Ihsan',
    'age' : 1.9
  },
  'child2' : {
    'name' : 'aftar',
    'age' : 1.11
  }
}

child3 = {
  'nama' : 'maulida',
  'age': 5
}
child4 = {
  'nama' : 'ihsan',
  'age': 2
}

my_child = {
  'child3' : child3,
  'child4' : child4
}
print(my_child)
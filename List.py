# List
thisListFruit = ['apel', 'mangga', 'pisang']
print(thisListFruit) # ['apel', 'mangga', 'pisang']

# Nilai Duplikat Pada List
fruit = ['manggis', 'mangga', 'nanas', 'mangga']
print(fruit)

# Panjang Isi List
fruits = ['apel', 'semangka', 'jeruk']
print(len(fruits)) # 3

# Tipe Data Apapun Pada List
listString = ['nama', 'alamat', 'tanggal']
listNumber = [1, 2, 3]
listBoolean = [True, False, True]
print(listString, listNumber, listBoolean)

# Tipe Data Campuran Pada List
listCampuran = ['Rusdiana', 29, True]
print(listCampuran[0], type(listCampuran[0]))
print(listCampuran[1], type(listCampuran[1]))
print(listCampuran[2], type(listCampuran[2]))

# def info_item(data_item):
#     result_item = []
#     for item in data_item:
#         result_item.append((item, type(item)))
#     return result_item

# my_list = ['satu', 2, True]
# result_info_item = info_item(my_list)
# print(result_info_item)

# Konstruktor List
thisListNew = list(('ayam', 12, True))
print(thisListNew, type(thisListNew))

# Memeriksa item dengan 'in'
listBarang = ['penghapus', 'pulpen']
if 'pulpen' in listBarang:
    print('yes, itu adalah alat untuk menulis')

# Ubah daftar item dengan melihat index
fruit = ['apple', 'mango', 'watermelon']
fruit[1] = 'pinaple'
print(fruit)

# Menyisipkan item dengan index yang ditentukan
list_insert = ['angga', 'asep', 'teguh']
list_insert.insert(0, 'muhammad')
print(list_insert) # ['muhammad', 'angga', 'asep', 'teguh']

# Menambahkan item di akhir list
list_append = ['suzuki', 'honda']
list_append.append('datsun')
print(list_append) # ['suzuki', 'honda', 'datsun']

# Menambahkan list lain ke list saat ini
list_1 = ['honda', 'suzuki']
list_2 = ['yaris', 'apv']
list_1.extend(list_2)
print(list_1) # ['honda', 'suzuki', 'yaris', 'apv']

# Hapus item tertentu pada list
list_remove = ['a', 'b', 'c']
list_remove.remove('a')
print(list_remove) # ['b', 'c']

# Hapus item yang ditentukan oleh index
list_pop = [1, 2, 3]
# list_pop.pop()
# jika parameter dikosongkan, pop menghapus item terakhir pada list
list_pop.pop(0)
print(list_pop) # [2, 3]

# Menghapus item yang di tentukan atau list sepenuhnya
list_del = [2, 3, 4]
del list_del[0]
print(list_del) # [3, 4]

list_del_non_parameter = [5, 6 , 7]
del list_del_non_parameter

# Membersihkan item list
list_clear = [6, 7, 8]
list_clear.clear()
print(list_clear) # []

# Iterasi list
list_loop = ['satu', 'dua', 'tiga']
for angka_list in list_loop:
  print(angka_list)
# satu
# dua
# tiga

# Iterasi list hanya no indexnya
list_index_loop = ['empat', 'lima', 'enam']
for index in range(len(list_index_loop)):
  print(index)
# 0
# 1
# 2

# Iterasi index dan item pada list
list_print_i_n = ['nol', 'satu', 'dua']
for i in range(len(list_print_i_n)):
    print(i, list_print_i_n[i])
# 0 nol
# 1 satu
# 2 dua

# Iterasi sementara
list_while = ['ayah', 'ibu', 'ihsan']
i = 0
while i < len(list_while):
  print(list_while[i])
  i += 1

# Pemahaman List
# newlist = [expresion for item in iterable if condition == True]
fruits = ['apple', 'melon', 'stawberry']
new_fruits = [x for x in fruits if 'a' in x]
# mengambil hanya buah yang memiliki nama 'a' saja yang di ambil (filter)
print(new_fruits)

# Tidak menggunakan pemahaman list
mobil = ['yaris', 'alpart', 'jimmny']
new_mobil = []

for x in mobil:
    if 'a' in x:
      new_mobil.append(x)

print(new_mobil)

# Memanipulasi dengan pemahaman list
karyawan = ['angga', 'asep', 'teguh']
new_karyawan = [x if x != 'teguh' else 'asep' for x in karyawan]
# kembalikan nama karyawan jika bukan teguh, jika teguh kembalikan asep
print(new_karyawan)


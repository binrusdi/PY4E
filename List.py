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
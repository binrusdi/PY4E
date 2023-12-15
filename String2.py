# Method String
word = 'rusdiana'

resultCapitalized = word.capitalize() # Huruf awal kapital
print(resultCapitalized) # Rusdiana

resultCasefold = word.casefold() # Huruf jadi kecil
print(resultCasefold)

resultCenter = word.center(20, '*') # Huruf ditengah
print(resultCenter) # ******rusdiana****** -> 20 karakter

resultCount = word.count('a') # berapa kali 'a' muncul
print(resultCount) # 2

resultEncode = word.encode() # mengkodekan string
print(resultEncode) # b'rusdiana'

resultEndswith = word.endswith('a') # apakah akhir string ada 'a'
print(resultEndswith) # True

words = 'rus\tdiana'
resultExpandtabs = words.expandtabs(3) # jarak tab pada string
print(resultExpandtabs) # rus   diana

teksFind = 'welcome mr'
resultFind = teksFind.find('mr') # mencari string, mengembalikan no index nya
print(resultFind) # 8

textFormat = 'masukan harga {}'
harga = 100000
resultFormat = textFormat.format(harga) # memasukan nilai int ke placholder '{}'
print(resultFormat) # masukan harga 100000

# Jenis Format
ayam = 'kami punya {:<8} ayam' # rekatkan ke kiri, beri ruang 8 karakter ke kanan
print(ayam.format(20)) # kami punya 20       ayam

domba = 'kami punya {:>10} domba' # rekatkan ke kanan, beri ruang 10 karakter ke kiri
print(domba.format(10)) # kami punya         10 domba

makan = 'setiap pagi saya harus makan {:^8} 1 porsi'
# simpan ditengah dengan jarak karakter kanan kiri 8
print(makan.format('ayam')) # setiap pagi saya harus makan   ayam   1 porsi
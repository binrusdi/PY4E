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

teksExpantabs = 'rus\tdiana'
resultExpandtabs = teksExpantabs.expandtabs(3) # jarak tab pada string
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

suhu = 'suhu di bandung sekarang antara {:+} dan {:+} celcius'
# menambahkan tanda minus atau plus
print(suhu.format(-7, 20))

suhu2 = 'suhu di pangalengan tidak menentu {:-} atau {:-} celcius'
# menambhakan karakter minus jika nilai minus, jika positif tidak ditampilkan apa2
print(suhu2.format(-1, 20))

teksIsalnum = 'company12'
resultIsalnum = teksIsalnum.isalnum() # memeriksa alphabet dan numerik
print(resultIsalnum) # True

teksIsalpha = 'ini bukan murni alp4bet'
resultIsalpha = teksIsalpha.isalpha()
print(resultIsalpha) # False

teksIsdigit = '2013'
resultIsdigit = teksIsdigit.isdigit() # memeriksa string adalah angka(digit)
print(resultIsdigit) # True

teksIslower = 'dian'
resultIslower = teksIslower.islower() # memeriksa apakah steing huruf kecil semua
print(resultIslower) # True
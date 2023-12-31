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
resultIslower = teksIslower.islower() # memeriksa apakah string huruf kecil semua
print(resultIslower) # True

teksIsnumeric = '23456'
resultIsnumeric = teksIsnumeric.isnumeric() # mencocokan apakah string berisi numerik
print(resultIsnumeric) # True

teksIsprintable = 'kamu mau\tkemana'
resultIsprintable = teksIsprintable.isprintable() # mencari tahu apakah string ini bisa dicetak
print(resultIsprintable) # False, karna '\t' tidak bisa dicetak

teksIsspace = ' '
resultIsspace = teksIsspace.isspace() # apakah variable hanya ada space saja
print(resultIsspace) # True

teksIstitle = 'Helo, Rusdiana'
resultIstitle = teksIstitle.istitle() # memeriksa apakah setiap kata diawali huruf besar
print(resultIstitle) # True

teksUpper = 'Nama dian'
resultUpper = teksUpper.isupper() # apakah semua string huruf besar
print(resultUpper) # False

teksJoin = ('kelinci', 'saya', 'berwarna', 'merah')
resultJoin = '->'.join(teksJoin)
# gabungkan semua item dalam tuple menjadi string dengan pemisah.
print(resultJoin) # kelinci->saya->berwarna->merah
# Catatan: Saat menggunakan kamus sebagai iterable, nilai yang dikembalikan adalah kuncinya, bukan nilainya.

teksLjust = 'banana'
resultLjust = teksLjust.ljust(20)
# menambahkan string banana menjadi 20 karakter dan string di tempatkan dikiri.
print(resultLjust, 'is fruit fav')

teksLstrip = '      kamu...'
resultLstrip = teksLstrip.lstrip()
# Mengembalikan string yang dipangkas kiri
print('apakah', resultLstrip)

teksPartition = 'saya makan salad'
resultPartition = teksPartition.partition('makan')
# mencari string yang di tentukan dan membagi string dalam tiga bagian tuple.
# pertama sebelum string yang ditentuka
# kedua string yang ditentukan
# ketiga setelah string yang di tentukan
print(resultPartition) # ('saya', 'makan', 'salad')

teksSplit = 'welcome to the jungle'
resultSplit = teksSplit.split()
# memisahkan string menjadi list dari setiap kata
print(resultSplit) # ['welcome', 'to', 'the', 'jungle']

teksSplitLine = 'welcome to the\n jungle'
resultSplitLine = teksSplitLine.splitlines()
# membagi sebuah string menjadi list, pemisahnya adalah \n
print(resultSplitLine) # ['welcom to the', 'jungle']

teksStartWith = 'hi, nama saya dian'
resultStartWith = teksStartWith.startswith('hi')
# mengembalikan True jika string dimulai dengan nilai yang ditentukan, jika tidak, False.
print(resultStartWith) # True

teksStrip = '   banana   '
resultStrip = teksStrip.strip()
# menghapus spasi kiri kanan diantara string
print(resultStrip) # banana

teksSwapCase = 'hALLO nAMA SAYA rUSDIANA'
resultSwapCase = teksSwapCase.swapcase()
# membalikan huruf kecil ke kapital, kapital ke kecil
print(resultSwapCase) # Hallo Nama saya Rusdiana

teksTitle = 'nama saya rusdiana'
resultTitle = teksTitle.title()
# huruf pertama setiap kata menjadi huruf besar
print(resultTitle) # Nama Saya Rusdiana

teksZfill = 'RUSDIANA'
resultZfill = teksZfill.zfill(10)
# menambahkan 0 di awal string sampai panjang karakter yang ditentukan
print(resultZfill) # 00RUSDIANA











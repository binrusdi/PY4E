# Mengiris String
word = 'Python'
print(word[0:]) # Python
print(word[0:3]) # Pyt
print(word[:len(word)]) # Python
print(word[-len(word):]) # Python
print(word[-6:]) # Python -> karena urutan akhir string adalah -1

# Memodifikasi string
upper_word = word.upper()
print('Ini method upper() mengganti ke huruf besar ->', upper_word) # Ini method upper() mengganti ke huruf besar -> PYTHON

lower_word = word.lower()
print('Ini method lower() mengganti ke huruf kecil ->', lower_word) # Ini method lower() mengganti ke huruf kecil -> python

strip_word = ' python '
result_strip_word = strip_word.strip()
print('Ini method strip() menghapus spasi awal dan akhir ->',result_strip_word) # Ini method strip() menghapus spasi awal dan akhir -> python

replace_word = word.replace('thon', 'char')
print('Ini menggunakan replace() asal nya Python -> ', replace_word) # Ini menggunakan replace() asal nya Python -> Pychar

split_word = 'Py,thon'
result_split_word = split_word.split(',') # Memisahkan string dengan tanda tertentu, menjadi 'list'
print(result_split_word) # ['Py', 'thon']

# Format String
nama = 'Rusdiana'
umur = 28
tempatLahir = 'Bandung'
words = 'Nama saya adalah {}, saya berumur {} dan lahir di kota {}'
result_words_1 = words.format(nama, umur, tempatLahir) # argumen harus sesuai urutan agar menempati placeholder ({}) yang benar
print(result_words_1) #Nama saya adalah Rusdiana, saya berumur 28 dan lahir di kota Bandung

company = 'suzuki' # index 0
tipe = 'mobil' # index 1
bahanBakar = 'bensin' # index 2
kalimat = 'saya membeli {1} merek {0} yang bahan bakarnya {2}'
result_kalimat = kalimat.format(company, tipe, bahanBakar) # dengan menggunakan index, penempatan sesuai index dalam placeholder, argumen diabaikan
print(result_kalimat) # saya membeli 'mobil' merek 'suzuki' yang bahan bakarnya 'bensin'

# Escape karakter
'''
\'  <- single quote
\\  <- backslash
\n  <- new line
\r  <- carriage return : Hello \rworld => Hello
                                        world
\t  <- tab
\b  <- backspace : Hello \bworld => Helloworld
'''
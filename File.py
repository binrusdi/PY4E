# Untuk bekerja dengan file di python kita mempunyai fungsi open()
# fungsi open() mengambil dua parameter
# open("namaFile", "mode")
# fungsi open() mengembalikan objek file
# Mode pada fungsi open( q)

# "r", baca -> membuka file untuk dibaca, jika tidak ada error
# "a", tambahkan -> membuka file untuk ditambahkan, membuat file jika tidak ada
# "w", menulis -> membuka file untuk ditulis, membuat file jika tidak ada, menimpa isi file yg ada
# "x", buat -> membuat file yg ditentukan, mengembalikan kesalahan jika file tsb ada

# Membaca File
# Penanganan file
# "t", untuk teks
# "b", untuk binner (misalnya gambar)
rf = open("file.txt", "rt")
# "rt" adalah mode baca dan teks
print(rf)

# Metode pada fungsi open()
# read(), mengembalikan semua isi teks file
print(rf.read())

# readline(), mengembalikan satu baris teks pada file
print(rf.readline())

"""Anda harus selalu menutup file anda, dalam beberapa kasus, karena buffering, perubahan yang dilakukan pada file tidak terlihat sampai anda menutupnya"""

# Menulis File
# Menulis ke file yang ada, tambahkan psrameter ke fungsi open()
# "a", append -> akan ditambshkan ke akhir file
# "w", tulid -> akan menimpa konten apapin yang sudah ada
tf = open("file.txt", "a")
tf.write("Apakah ini tambahan kata?")
tf.close()
# buka dan baca setelah menambahkan isi
bf = open("file.txt", "r")
print(bf.read())
